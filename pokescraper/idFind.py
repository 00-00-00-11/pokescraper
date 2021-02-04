import requests


def findId():
  base_url = 'http://breakinbox.com/hanukkah-'
  for i in range(2300, 9999):
    print(i)
    url = base_url + str(i)
    x = requests.get(url)
    if x.status_code == 200:
      print(url)
      break

findId()