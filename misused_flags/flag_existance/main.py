import argparse
import logging
import os
import sys

import requests

from misused_flags.flag_existance import consts
from misused_flags.flag_existance.runner import RunnerThread


def pars_args(arguments):
  parser = argparse.ArgumentParser(
    description='analyze missue by children')
  parser.add_argument('-yubi', '--yubikey',
                      help='yubi hash',
                      type=str,
                      required=True, default="")

  return parser.parse_args(arguments)


def get_sites():
  return [0, 3, 203, 215, 2, 15, 100, 205]


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
  categories = open("categories", "r")

  f = open("RESULTS", "a")
  f.write("SITE,CATEGORY,FLAG_ID,HAS_FLAG\n")
  threads = []
  max = 0
  for category in categories:
    if max < 20:
      thread = RunnerThread([category.replace('\n', ''), sites, f])
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
