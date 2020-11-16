#!/usr/bin/env python3
#  _  _ _|  _   _
# (_ | (_| |_) (_|
#          |
# scraper to search for item on sale in a specific page
# this script was made to run in a cronjob, that's why i use absolute paths
#
# scraper para encontrar item em promoção em determinada página
# este# script foi feito para rodar em um cronjob, por isso utilizei
# caminho absoluto ao chamar o subprocesso de notificação

import urllib.request
from bs4 import BeautifulSoup
import re
import subprocess
import argparse


def read_page(url):
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:82.0)" \
                 "Gecko/20100101 Firefox/82.0"
    headers = {"User-Agent": user_agent}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    page_string = soup.get_text()
    return page_string


def find_item(items, page_string):
    items_string = "|".join(items)
    search_query = re.compile(items_string, re.IGNORECASE)
    items_found = search_query.findall(page_string)
    items_found = list(dict.fromkeys(items_found))
    return items_found


def notify(items_found):
    if not items_found:
        quit()
    else:
        items = ", ".join(items_found)
        subprocess.Popen(["/usr/bin/notify-send", "-u", "critical",
                          "{} em promoção!".format(items)])


def main():
    parser = argparse.ArgumentParser(description="Search for items on sale.")
    parser.add_argument("-i", "--items", type=str, required=True, nargs="+",
                        help='item(s) to search')
    parser.add_argument("-u", "--url", type=str, required=True, help='url')
    args = parser.parse_args()
    items = args.items
    url = args.url
    html = read_page(url)
    results = find_item(items, html)
    notify(results)


if __name__ == "__main__":
    main()
