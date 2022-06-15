from lib import get_links_on_page,get_page_content,extract_gtm, extract_ym,do_excel
import sys

# получаем домен при запуске скрипта из консоли
# if len(sys.argv) != 2:
#     print("Введите url")
# domain = sys.argv[1]
domain = 'https://kokoc.com'
page_content = get_page_content(domain)
main_gtm = extract_gtm(page_content)
main_ym = extract_ym(page_content)
linksonpage = get_links_on_page(page_content, domain)
downloadedlinks = set()
result = {}
newlinks = set()
cnt = 0

while linksonpage:
        url = list(linksonpage)[0]
        linksonpage.remove(url)
        if url.count('/') <= 3 and len(downloadedlinks) < 5:
            downloadedlinks.add(url)
        # получаем наличие GTM на странице
            if main_gtm or main_ym in get_page_content(url):
                result[url] = main_gtm, main_ym
            else:
                result[url] = "Нет счетчиков"
            cnt +=1
        # получем ссылки на итерируемой странице
            newlinks = get_links_on_page(page_content, domain+url)
        # кладем в множество для рбхода те страницы, где еще не были
            linksonpage |= newlinks - downloadedlinks
        else:
            break
do_excel(result)



