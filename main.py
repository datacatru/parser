import requests
import re
from bs4 import BeautifulSoup

# скачиваем страницу
url = 'https://medicinadeti.ru/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

# что ищем
match = re.search(r'ym\([0-9]+,', req) # если с импутом то через f строку

# тут список страниц для обхода
uniq_page = []
# цикл и условия добавления страниц в список uniq_page
for link in soup.find_all('a'):
    if len(uniq_page) < 5:
        pages = link.get('href')
        if pages:
            pages = pages.split('#')[0]
        if pages:
            if url in pages:
                pages = pages.replace(url,'')
        if pages.startswith('http') or pages.startswith('mail') or pages.startswith('tel'):
            continue
        uniq_page.append(pages)
    else:
        break

# цикл проверки счетчика на страницах их списка
for i in uniq_page:
        checkUrl = requests.get(url + i).text
        if match.group(0) in checkUrl:
            print(i,': yes')


'''
    # сохраняем страницу как файл
    with open('med.html', 'w') as file:
        file.write(req)

if match:
    print(match.group(0))

'''