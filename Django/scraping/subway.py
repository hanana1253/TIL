import requests
from bs4 import BeautifulSoup

url = 'https://www.subway.co.kr/menuList/sandwich'

def returnSoup(url):
    response = requests.get(url)
    html_text = response.text
    return BeautifulSoup(html_text, 'html.parser')

soup = returnSoup(url)
menu_a_tags = soup.select('#content > div > div.pd_list_wrapper > ul > li > a.btn_view')

for a_tag in menu_a_tags:
    menu_id = a_tag['data-menuitemidx']
    menu_data = { f'{menu_id}': dict() }
    menu_soup = returnSoup(f'https://www.subway.co.kr/menuView/sandwich?menuItemIdx={menu_id}')
    menu_name = menu_soup.select_one('#content > div > div.hd > h2').text
    menu_kcal = menu_soup.select_one('#content > div > div.hd > p.cal').text
    menu_data[f'{menu_id}'] = {
        'code': menu_id,
        'name': menu_name,
        'kcal': menu_kcal
    }
    print(menu_data)



# headers = {
#     'authority': 'www.subway.co.kr',
#     'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-dest': 'document',
#     'referer': 'https://www.subway.co.kr/',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
#     'cookie': '_fbp=fb.2.1613626779419.182964328; _ga=GA1.3.771829997.1613626780; _gid=GA1.3.1731865333.1618556913; popup24=Y',
# }

# response = requests.get('https://www.subway.co.kr/menuList/sandwich', headers=headers)
# html_text = response.text
# soup = BeautifulSoup(html_text, 'html.parser')


