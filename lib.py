import requests
import re
from bs4 import BeautifulSoup
import pandas


def get_page_content(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.text

def extract_gtm(page_content):
    match = re.search(r'GTM-[0-9a-zA-Z]+', page_content, re.DOTALL)
    if match is not None:
        return match.group(0)
    return "GTM не найден"

def extract_ym(page_content):
    match = re.search(r'ym\([0-9]+,', req)
    if match is not None:
        return match.group(0)
    return "YM не найден"

def get_links_on_page(page_content, domain):
    # тут список страниц для обхода
    uniq_page = set()
    soup = BeautifulSoup(page_content, 'html.parser')
    # цикл и условия добавления страниц в список uniq_page
    for link in soup.find_all('a'):
        if len(uniq_page) < 5:
            url = link.get('href')
            if url:
                url = url.split('#')[0]
            if url:
                if domain in url:
                    url = url.replace(domain, '')
            if url.startswith('http') or url.startswith('mail') or url.startswith('tel'):
                continue
            uniq_page.add(url)
        else:
            break
    return uniq_page


#def get_sitemap(page_content):
    # сделать парсинг карты сайта https://lxml.de/parsing.html

