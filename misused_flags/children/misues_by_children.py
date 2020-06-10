import argparse
import logging
import os
import sys

import requests

from cfe.misused_flags.children import consts
from cfe.misused_flags.children.runner_thread import RunnerThread


def pars_args(arguments):
  parser = argparse.ArgumentParser(
    description='analyze missue by children')
  parser.add_argument('-yubi', '--yubikey',
                      help='yubi hash',
                      type=str,
                      required=True, default="")

  return parser.parse_args(arguments)


def get_sites():
  sites_uri = "http://catsvc.vip.ebay.com/catalog/v1/category_tree/get_tree_version?"
  headers = {"Content-Type": "application/json", "Authorization": f"Bearer {consts.SVC_AUTH_TOKEN}" }
  sites_response = requests.get(sites_uri,
                                headers=headers,
                                verify=False)
  category_tree_versions = sites_response.json()['categoryTreeVersions']
  return category_tree_versions.keys()


def get_tree_for_site(site):
  tree_uri = f'http://catsvc.vip.ebay.com/catalog/v1/category_tree/{site}/get_tree'
  headers = {"Content-Type": "application/json", "Authorization": f"Bearer {consts.SVC_AUTH_TOKEN}", "X-EBAY-REQUEST-CONTROL": '{normalizedFeatures:"true"}' }
  tree_response = requests.get(tree_uri,
                                headers=headers,
                                verify=False)
  return tree_response.json()['categoryNode']


def get_catsvc_token():
  token_uri = "http://www.auth.stratus.ebay.com/idauth/site/token?client_id=urn:ebay-marketplace-consumerid:dd6323b9" \
              "-45ee-4fb9-8e6f-7c69aaa4275c&client_secret=8b4986fc-9823-4723-abff-44887856dfaf&grant_type" \
              "=client_credentials&scope=https://api.ebay.com/oauth/scope/core@application "
  headers = {"Content-Type": "application/json"}
  token_response = requests.get(token_uri,
                                headers=headers,
                                verify=False)
  return token_response.json()['access_token']


def analyze(sites):
  f = open("report_children_9", "a")
  f.write("SITE,PARENT_ID,LEVEL,FLAG_ID\n")
  threads = []
  max = 0
  for site in sites:
    tree = get_tree_for_site(site)
    if max < 20:
      thread = RunnerThread([tree, site, f])
      thread.start()
      threads.append(thread)
      max += 1
    else:
      for t in threads:
        t.join()
      max = 0
      threads.clear()

  for t in threads:
    for t in threads:
      t.join()

  f.close()


def run(arguments):
  args = pars_args(arguments)
  os.environ[
    'http_proxy'] = f'http://{args.yubikey}@c2syubi.vip.ebay.com:8080'
  print(os.environ['http_proxy'])
  consts.SVC_AUTH_TOKEN = get_catsvc_token()
  sites = get_sites()
  analyze(sites)


if __name__ == '__main__':
  logging.basicConfig(format='%(levelname)-7s %(asctime)s - %(message)s',
                      stream=sys.stdout, level='INFO')
  run(sys.argv[1:])
