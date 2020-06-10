#!/usr/bin/python3

import logging
import threading

import requests

from misused_flags.flag_existance import consts


class RunnerThread(threading.Thread):
  def __init__(self, args=()):
    threading.Thread.__init__(self)
    self.category = args[0]
    self.sites = args[1]
    self.file = args[2]

  def run(self):
    print("Starting " + self.name)
    analyze(self.category, self.sites, self.file)


def analyze(category, sites, file):
  for site in sites:
    logging.info(f'{site} {category}')
    service_response = call_service(category, site)
    if service_response is None:
      continue

    threadLock.acquire()
    file.write(f'{service_response}\n')
    file.flush()
    threadLock.release()


def call_service(category, site):
  service_response = do_call(site, category)
  if service_response.status_code == 200:
    return is_flag_present(category, site, service_response)


def do_call(site, category):
  headers = {"Authorization": f"Bearer {consts.SVC_AUTH_TOKEN}", "X-EBAY-REQUEST-CONTROL": '{normalizedFeatures:"true"}'}
  service_call = f"http://catsvc.vip.ebay.com/catalog/v1/category_tree/{site}/category/{category}?features=allFlags"

  content_response = requests.get(service_call,
                                  headers=headers,
                                  verify=False)
  return content_response;


def is_flag_present(category, site, service_response):
  flags = service_response.json()['features']
  for flag in flags:
    flag_id = flag['id']
  if flag_id == 386:
    return f'{site},{category},386,YES'
  if flag_id == 400:
    return f'{site},{category},400,YES'

  return None


def is_expected_value(flag_id, flag_value_from_svc, actual_value):
  values = flag_value_from_svc['value']
  for val in values:
    if flag_id == 386:
      if val['name'] == actual_value or val['helpId'] == actual_value:
        return True

    if flag_id == 400:
      if val['name'] == actual_value or val['helpId'] == actual_value:
        return True

    return False


threadLock = threading.Lock()
