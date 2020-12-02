import re
import urllib
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

image_pattern = re.compile(r'http*://pocketmonsters.co.il/wp-content/uploads/.*\.jpg')
title_pattern = re.compile(r'<span itemprop="name">(.*?)פוקידע: פוקימון \d* – ')


def scrape():
  home_url = 'https://www.pocketmonsters.co.il/?p=19967'
  soup = parse_page(home_url)
  divs = soup.findAll("div", {"class": "post-inner"})
  for div in divs:
    links = div.findAll('a')
    for a in links:
      try:
        page_ref = a['href']
        if page_ref.startswith('http://www.pocketmonsters.co.il'):
          soup = parse_page(page_ref)
          html = str(soup)
          url_results = image_pattern.findall(html)
          spans = soup.findAll("span", {"itemprop": "name"})
          name_part = str(spans[0])
          g = re.search(r'<span itemprop="name">(.*?)<\/span>', name_part)
          first = g.group(1)[0:g.group(1).index(' / ')]
          second = first.replace('פוקידע: פוקימון', '').replace(' – ', '')
          final_name = re.sub(" \d+", " ", second).strip()
          print(final_name)
          print(url_results[0])
          urllib.request.urlretrieve(url_results[0], f'/Users/eoren/pokemon/{final_name}.jpg')


      except:
        print("Invaid URL")

  # print(pages)


def parse_page(url):
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup


if __name__ == '__main__':
  scrape()
