import requests
from bs4 import BeautifulSoup
import requests

headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'iframe',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'referer': 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=159074&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
    'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=75ZMCSOJFICGA; nid_inf=1156331681; NID_AUT=MvXOZ8d5CebxvgrA0wN9T+2VjEnqr0PLOPuOjQY6oOvmxpWKKBwvBaD9lgGjSLyp; NID_JKL=8mXxUTLG98bJlUMSqEYCWZuP/AG7JwPxC41J+mhDupE=; nx_ssl=2; JSESSIONID=29D89A4C139BD0E938E6B073C6EA562B; NDARK=Y; BMR=s=1618537572461&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dgnsehfvlr%26logNo%3D220667438541%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hcDbzdprvhGssCEBFkdssssssYw-208228; NID_SES=AAABpuWrTRYpik7yC3NvDxMRuRCBJYDwejgl90HopRG9LFibYC1xw2SNAHBb9E9E2ldQUDNR9LgO3wQJ460HlslaXdTtLudqgoBFiBnYtoaDXXNEnlvlsyauFsY3XtM0viIblBhV5OQfoiMLGUR0KOO9ly0BP9jqT51wmwRzqme9WKJ6r4I59KJB7I7KCcga+/2/aHgf/ig+35GvOBusZhuSHV5ImhwapOnJGmM0tJz8WdPT4oAMiPTl15TdTCSupUTCnYjvBQt3yclXY3SkmXgE0y4TA1mIQJkHWJ7+nU2su03EAB9ghDBKBstqlU5zbeE6fvqjhWw3l9EbHZgwnpBLC+6DgvhcTDlose9UtWifRndWseuOUkt2Z8RJwA+sspVVhg0u9fXuCKE8PHTgevHz1KSUlm9aLwSSl9qBs/W6ss81LoKi0SdwcUCzIdk4MXdC9gRVFrwV7p6VYIR6KGFsppV54Ttv//D7GJk/b3Ao9FxmwLYC11TZOR38vFtGiUTatP5gIG8Oo549s/TYrvYX6W8bmyy3/75YF58jlOj03zcxoNq7qjeftDCYXhCzQlP1Fg==; csrf_token=769e9d64-a752-49ac-bad2-b261face5341',
}


for startnum in range(1, 10):
    params = (
        ('code', '159074'),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
        ('page', f'{startnum}'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    comment_lis = soup.select('body > div > div > div.score_result > ul > li')

    count = 0
    for li in comment_lis:
        comment = li.select_one(f'#_filtered_ment_{count}').text.strip()
        if li.select('span._unfold_ment'):
            comment = li.select_one('span._unfold_ment > a')['data-src']
        count += 1
        print(comment)
