from lib import get_links_on_page,get_page_content,extract_gtm

domain = 'https://medicinadeti.ru/'
page_content = get_page_content(domain)
main_gtm = extract_gtm(page_content)
pages = get_links_on_page(page_content, domain)

for i in pages:
    if main_gtm:
        print(i, main_gtm)