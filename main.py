from lib import get_links_on_page,get_page_content,extract_gtm, extract_ym
import xlsxwriter
import pandas

domain = 'https://medicinadeti.ru/'
page_content = get_page_content(domain)
main_gtm = extract_gtm(page_content)
main_ym = extract_ym(page_content)
pages = get_links_on_page(page_content, domain)
all_pages = []
result = {}

# получаем наличие GTM по ссылкам на странице
for i in pages:
    if main_gtm or main_ym: # не корректное условие, что если ни того ни другого? Или только одно?
        result[i] = main_gtm, main_ym
print(result)

# Делаем DataFrame
df = pandas.DataFrame.from_dict(result,'index').reset_index()
df.columns = ['PageUrl', 'GTM', 'YM']
print(df)

# Сохраняем в excel
writer = pandas.ExcelWriter('parser.xlsx', engine='xlsxwriter')
df.to_excel(writer)
writer.save()

'''
попытки получить все страницы сайта
for elem in pages:
    all_pages.append(elem)
print(all_pages)

for i in all_pages:
    content = get_page_content(domain + i) # получаем контент новой страницы

print(content)

            nextpage = get_links_on_page(content, domain) # получем новый список урлов
            for k in nextpage:
                all_pages.appenf(k)
print(all_pages)

   # for nelem in nextpage:
    #    all_page.add(nelem)



if len(all_pages)<15:
    for elem in all_pages:
        elem = pa
        for url in pages:
            all_pages.add(url) # для каждого урл из множества pages добавить элемент в all_pages
print(all_pages)
'''






#all_pages = get_all_pages()
