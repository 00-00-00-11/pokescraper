#!/usr/bin/python3

import logging
import threading

import requests

from cfe.misused_flags.ansectors import consts


class RunnerThread(threading.Thread):
  def __init__(self, args=()):
    threading.Thread.__init__(self)
    self.cand = args[0]
    self.file = args[1]

  def run(self):
    print("Starting " + self.name)
    analyze(self.cand, self.file)


def analyze(cand, file):
  level = -1
  new_level_with_cand = call_service(cand, level, None)
  logging.info(f'{cand} {new_level_with_cand}')
  if new_level_with_cand is not None and new_level_with_cand[1] > 0:
    logging.info('Adding to report')
    res = [cand, new_level_with_cand]
    threadLock.acquire()
    file.write(f'{res}\n')
    file.flush()
    threadLock.release()


def call_service(cand, level, prev_cand):
  site = cand[0].replace('"', '')
  category = cand[1].replace('"', '')
  flag = cand[2].replace('"', '')
  flag_value = cand[3].replace('"', '')
  char = extract_char(cand)
  service_response = do_call(site, category)
  if service_response.status_code != 200:
    logging.error(f'Candidate {cand} had errors: ' + extract_errors(service_response))
    return

  if int(category) == 0:
    return [prev_cand, level]

  if is_flag_present(service_response, flag, flag_value, char):
    level += 1
    category = service_response.json()['category']
    if 'ancestors' not in category:
      logging.info(f'No ancestors to {cand}')
      return
    else:
      ancestors = category['ancestors']
      for anc in ancestors:
       ans_cand = [site, anc, flag, flag_value, char]
       return call_service(ans_cand, level, cand)

  else:
    return [prev_cand, level]


def do_call(site, category):
  headers = {"Authorization": f"Bearer {consts.SVC_AUTH_TOKEN}"}
  service_call = f"http://catsvc.vip.ebay.com/catalog/v1/category_tree/{site}/category/{category}?features=allFlags"

  content_response = requests.get(service_call,
                                  headers=headers,
                                  verify=False)
  return content_response;


def is_flag_present(service_response, flag_id, flag_value, char):
  flags = service_response.json()['features']
  for flag in flags:
    if flag['id'] != int(flag_id):
      continue

    flag_value_from_svc = flag['value']
    if flag_value_from_svc['valueType'] == 'Boolean':
      if flag_value_from_svc['value'] == bool(float(flag_value)):
        return True
    else:
        if char is not None:
          values = flag_value_from_svc['value']
          for val in values:
            if ('name' in val and val['name'] == char) or ('helpId' in val and val['helpId'] == char):
              return True
        else:
          if str(flag_value_from_svc['value']) == flag_value:
            return True
  return False


def extract_char(cand):
  if cand[4] is None:
    return None
  no_quads = cand[4].replace('""', '')
  return None if not no_quads.strip() else no_quads.replace('"', '')


def extract_errors(service_response):
  if service_response is None:
    return ""
  json = service_response.json()
  if 'errors' in json:
    return json['errors'][0]['message']
  else:
    if 'warnings' in json:
      return json['warnings'][0]['message']
    else:
      return ""


threadLock = threading.Lock()
