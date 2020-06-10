#!/usr/bin/python3

import threading

import requests

from cfe.misused_flags.children import consts, config
import logging


class RunnerThread(threading.Thread):
  def __init__(self, args=()):
    threading.Thread.__init__(self)
    self.tree = args[0]
    self.site = args[1]
    self.file = args[2]

  def run(self):
    print("Starting " + self.name)
    analyze(self.tree, self.site, self.file)


def equals(site, parent_children, parent_flags, child_to_flags):
  report = []
  for parent_flag in parent_flags:
    if parent_flag is not None and bool(child_to_flags):
      matches = len(child_to_flags)
      try:
        for ctf in child_to_flags:
          if parent_flags[parent_flag] == child_to_flags[ctf][parent_flag]:
            matches -= 1

        if matches == 0:
          logging.info(f"Flag {parent_flag} is identical ")
          prnt_splt= parent_children.split('_')
          report.append(f"{site},{prnt_splt[0]},{prnt_splt[1]},{parent_flag}")
      except:
        continue

  return report


def analyze(tree, site, file):
  parent_child_map = map_parent_to_chilred(tree)
  for parent_children in parent_child_map:
    parent_flags = extract_category_flags(site, parent_children);
    child_to_flags = {}
    for child in parent_child_map[parent_children]:
      logging.info(f"Site {site} Comparing child {child} to parent {parent_children}")
      child_to_flags[child] = extract_category_flags(site, child)

    res = equals(site, parent_children, parent_flags, child_to_flags)

    threadLock.acquire()
    for r in res:
      file.write(f'{r}\n')
    file.flush()
    threadLock.release()


def traverse_children(children, map):
  for child in children:
    category_ = child['category']
    if 'children' in category_:
      # add flag here
      map[f"{category_['id']}_{category_['level']}"] = category_['children']
      traverse_children(child['children'], map)


def map_parent_to_chilred(tree):
  #add flag here
  map = {f"{tree['category']['id']}_{tree['category']['level']}": tree['category']['children']}
  traverse_children(tree['children'], map)
  return map


def extract_category_flags(site, parent):
  flag_map = {}
  try:
    headers = {"Authorization": f"Bearer {consts.SVC_AUTH_TOKEN}", "X-EBAY-REQUEST-CONTROL": '{normalizedFeatures:"true"}'}
    service_call = f"http://catsvc.vip.ebay.com/catalog/v1/category_tree/{site}/category/{parent.split('_')[0]}?features=allFlags"

    content_response = requests.get(service_call,
                                  headers=headers,
                                  verify=False)

    reponse = content_response.json()
    if 'features' in reponse:
      flags = content_response.json()['features']
      for flag in flags:
        if flag['id']in config.INCLUDED_FLAGS:
          flag_map[flag['id']] = flag['value']

  except:
    logging.error(f"No Response returned site:{site} - parent{parent}")

  return flag_map


threadLock = threading.Lock()
