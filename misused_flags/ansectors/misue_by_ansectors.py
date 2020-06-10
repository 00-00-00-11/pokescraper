import csv
import logging
import sys
import os
import argparse
import requests

from cfe.misused_flags.ansectors import consts
from cfe.misused_flags.ansectors.runner_thread import RunnerThread


def pars_args(arguments):
  parser = argparse.ArgumentParser(
    description='analyze missue')
  parser.add_argument('-yubi', '--yubikey',
                      help='yubi hash',
                      type=str,
                      required=True, default="")

  return parser.parse_args(arguments)


def read_csv():
  paires = []
  with open('site_15_flag_720.csv', newline='') as csvfile:
    csv_content = csv.reader(csvfile, delimiter=',', quotechar='\\')
    for row in csv_content:
      paires.append(row)

    return paires


def get_catsvc_token():
  token_uri = "http://www.auth.stratus.ebay.com/idauth/site/token?client_id=urn:ebay-marketplace-consumerid:dd6323b9" \
              "-45ee-4fb9-8e6f-7c69aaa4275c&client_secret=8b4986fc-9823-4723-abff-44887856dfaf&grant_type" \
              "=client_credentials&scope=https://api.ebay.com/oauth/scope/core@application "
  headers = {"Content-Type": "application/json"}
  token_response = requests.get(token_uri,
                                headers=headers,
                                verify=False)
  return token_response.json()['access_token']


def analyze(candidates):
  consts.SVC_AUTH_TOKEN = get_catsvc_token()
  f = open("report_720", "a")
  threads = []
  max = 0
  for cand in candidates:
    max += 1
    if max < 10:
      thread = RunnerThread([cand, f])
      thread.start()
      threads.append(thread)
    else:
      for t in threads:
        t.join()
      max = 0
      threads.clear()

  f.close()


def run(arguments):
  args = pars_args(arguments)
  os.environ[
    'http_proxy'] = f'http://{args.yubikey}@c2syubi.vip.ebay.com:8080'
  print(os.environ['http_proxy'])

  candidates = read_csv()
  analyze(candidates)


if __name__ == '__main__':
  logging.basicConfig(format='%(levelname)-7s %(asctime)s - %(message)s',
                      stream=sys.stdout, level='INFO')
  run(sys.argv[1:])
