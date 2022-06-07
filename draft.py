import requests
import re
from bs4 import BeautifulSoup
import pandas

# скачиваем страницу
url = 'https://medicinadeti.ru/'
req = requests.get(url).text

result = {}

# что ищем
match = re.search(r'ym\([0-9]+,', req) # если с импутом то через f строку

# тут список страниц для обхода
uniq_page = set()
soup = BeautifulSoup(page_content, 'html.parser')
# цикл и условия добавления страниц в список uniq_page
for link in soup.find_all('a'):
    if len(uniq_page) < 10:
        pages = link.get('href')
        if pages:
            pages = pages.split('#')[0]
        if pages:
            if url in pages:
                pages = pages.replace(url,'')
        if pages.startswith('http') or pages.startswith('mail') or pages.startswith('tel'):
            continue
        uniq_page.add(pages)
    else:
        break

# цикл проверки счетчика на страницах их списка
for i in uniq_page:
        checkUrl = requests.get(url + i).text
        if match.group(0) in checkUrl:
            result[i] = 'yes'
df = pandas.DataFrame.from_dict(result,'index').reset_index()
df.columns = ['PageUrl', 'Counter']
print(df)

''' обход всех страниц сайта
1. в переменную url подставить следующее значение из списка
2. собрать все линки на новой странице только в том, случае, если их еще нет в списке юников
3. добавить новые линки к юникам
4. перейти к следующей странице, пока не будут собраны все страницы сайта
5. уже по полному списку юников делать проверку счетчика
'''
'''
дока: https://xlsxwriter.readthedocs.io/example_pandas_simple.html#ex-pandas-simple
writer = pandas.ExcelWriter('parser.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

??? отдает ошибку что нет модуля с названием движка

Зачем открывать и сохранять странцу, не поняла
    # сохраняем страницу как файл
    with open('med.html', 'w') as file:
        file.write(req)

if match:
    print(match.group(0))
'''