from lib import get_links_on_page,get_page_content,extract_gtm, extract_ym,do_excel
import sys

if len(sys.argv) != 2:
    print("Введите url")
domain = sys.argv[1]
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
do_excel(result)



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

вопросы:
+ по умолчанию инициализируется main файл?
+ как массово закоментить? ctr + /
- парсинг xml или обход всего сайта - не получилось
если по логике с множеством - наталкиваюсь на то, что с новой страницы грузятся те же самые урлы
и я не поняла, как его заставить получать новые ссылки. 
+ реадми зачем?
'''






#all_pages = get_all_pages()
