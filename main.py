import requests
import re
from bs4 import BeautifulSoup

# скачиваем страницу
url = 'https://medicinadeti.ru/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
uniq_page = []
for link in soup.find_all('a'):
   pages = link.get('href')
   if pages:
       pages = pages.split('#')[0]
   if pages:
       if url in pages:
           pages = pages.replace(url,'')
       if pages.startswith('http') or pages.startswith('mail') or pages.startswith('tel'):
           continue
   uniq_page.append(pages)
print(uniq_page)



'''
# перечень страниц
pages = []

# сохраняем страницу как файл
with open('med.html', 'w') as file:
    file.write(req)

# что ищем
match = re.search(r'ym\([0-9]+,', req) # если с импутом то через f строку

if match:
    print(match.group(0))

'''