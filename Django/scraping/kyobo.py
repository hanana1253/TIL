import requests
from bs4 import BeautifulSoup
import os

def getBookInfosByPage(page_num):

    cookies = {
        '$Cookie: WMONID': 'ggdGFeR2JOH',
        'PCID': '16189029358499752602816',
        'RB_PCID': '1618902935984243955',
        '_ga': 'GA1.3.1889568410.1618902938',
        '_gid': 'GA1.3.661530237.1618902938',
        'EG_GUID': '9737febb-531a-4daa-bd87-e65b7d7b21bf',
        'KYOBOSESSIONID': 'g21TJl7RVnjkjvGBbpF2StZXL1WfG4d8rCl22P4VhhLkmRvnLnrL\\u0021-503524961\\u0021-2124087674\\u00217300\\u0021-1\\u00211509789158\\u0021-2124087675\\u00217300\\u0021-1',
        'nowSeeList': f"9791188331796\\u0021@KOR\\u0021@%2Fimages%2Fbook%2Fmedium%2F796%2Fm9791188331796.jpg\\u0021@%B5%B7%C0%C7+%BC%D3%BC%BA%28150%BC%E2+%B1%E2%B3%E4...#9788901249599\\u0021@KOR\\u0021@%2Fimages%2Fbook%2Fmedium%2F599%2Fm9788901249599.jpg\\u0021@%C1%FA%BC%AD+%B3%CA%B8%D3",
        'RB_SSID': 'ut7CBcS2nV',
        'recentSch': '%uD30C%uC774%uC36C%24%5E%7C04.20%24%7C',
        'NSC_wjs_lzpcp_Dppljf': 'ffffffffd0b53b3045525d5f4f58455e445a4a423660',
        'welBigBan': 'done',
        'welcomePopup1': 'done',
        'clickorder': 'JAR',
        '_gat': '1',
        'wcs_bt': 's_453f4415ebcb:1618904314',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?linkClass=3315&mallGb=KOR&orderClick=JAR',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
    }

    params = (
        ('targetPage', f'{page_num}'),
        ('linkClass', '3314'),
        ('mallGb', 'KOR'),
        ('orderClick', 'JAR'),
    )

    response = requests.get('http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf', headers=headers, params=params, cookies=cookies, verify=False)

    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    books = soup.select('#prd_list_type1 > li> div > div.info_area > div.detail > div.title > a')

    for book in books:
        title = book.text
        print(book['href'].split("3314")[1])
        # code = book['href'].split('barcode=')[1]
        print(title)

for i in range(1, 2):
    getBookInfosByPage(i)
    print('Page', i)

def getReview(book_code, page_num):
    cookies = {
        '$Cookie: WMONID': 'ggdGFeR2JOH',
        'PCID': '16189029358499752602816',
        'RB_PCID': '1618902935984243955',
        '_ga': 'GA1.3.1889568410.1618902938',
        '_gid': 'GA1.3.661530237.1618902938',
        'EG_GUID': '9737febb-531a-4daa-bd87-e65b7d7b21bf',
        'KYOBOSESSIONID': 'g21TJl7RVnjkjvGBbpF2StZXL1WfG4d8rCl22P4VhhLkmRvnLnrL\\u0021-503524961\\u0021-2124087674\\u00217300\\u0021-1\\u00211509789158\\u0021-2124087675\\u00217300\\u0021-1',
        'recentSch': '%uD30C%uC774%uC36C%24%5E%7C04.20%24%7C',
        'welBigBan': 'done',
        'welcomePopup1': 'done',
        'clickorder': 'JAR',
        'nowSeeList': f"9791188331796\\u0021@KOR\\u0021@%2Fimages%2Fbook%2Fmedium%2F796%2Fm9791188331796.jpg\\u0021@%B5%B7%C0%C7+%BC%D3%BC%BA%28150%BC%E2+%B1%E2%B3%E4...#9788901249599\\u0021@KOR\\u0021@%2Fimages%2Fbook%2Fmedium%2F599%2Fm9788901249599.jpg\\u0021@%C1%FA%BC%AD+%B3%CA%B8%D3#$9791160504439\\u0021@KOR\\u0021@%2Fimages%2Fbook%2Fmedium%2F439%2Fm9791160504439.jpg\\u0021@%B8%F0%B4%F8+%C0%DA%B9%D9%BD%BA%C5%A9%B8%B3%C6%AE+%C0%D4...",
        'NSC_wjs_lzpcp_Dppljf': 'ffffffffd0b53b3045525d5f4f58455e445a4a423660',
        'RB_SSID': 'ut7CBcS2nV',
        'wcs_bt': 's_453f4415ebcb:1618905127',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=3314&barcode=9791160504439',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
    }

    params = (
        ('gb', 'klover'),
        ('barcode', f'{book_code}'),
        ('ejkGb', 'KOR'),
        ('mallGb', 'KOR'),
        ('sortType', 'like'),
        ('pageNumber', f'{page_num}'),
        ('orderType', 'order'),
    )

    response = requests.get('http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf', headers=headers, params=params, cookies=cookies, verify=False)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    reviews = soup.select('dl > dd.comment')
    for review in reviews:
        print(review.text)



getReview(9791160504439, 2)