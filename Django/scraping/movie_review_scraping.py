import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'movie.naver.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': f'https://movie.naver.com/movie/bi/mi/point.nhn?code=189075',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
    'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=75ZMCSOJFICGA; nid_inf=1156331681; NID_AUT=MvXOZ8d5CebxvgrA0wN9T+2VjEnqr0PLOPuOjQY6oOvmxpWKKBwvBaD9lgGjSLyp; NID_JKL=8mXxUTLG98bJlUMSqEYCWZuP/AG7JwPxC41J+mhDupE=; nx_ssl=2; BMR=s=1618284642254&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dchsmanager%26logNo%3D220922961706%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=hciIWsprvN8ssOLV24sssssstA8-144294; NID_SES=AAABpEUhX15rJ5Z591tdlwJl1Zj0/GfCv2fv8HrJ0C2rGhFX6FFqq2gr+SRdPPRklo5EHPROZP6lZFa32eDNlXqFAKo4WyyxB8o9StLFeh+MvvxuBXiC/PS21+WVdDkeFlipp+Ezvja5eNwoOFf1isbJcosDRuxn09NYaMc/HDuhg05XjyrWRuQCkoZUpdoFXZxFY76OBPiv2R6QZ0yrIViFHrCDv9lBR/Nfud/KKTSdEI2pGORSDCPhUyBMP8pI6aNGbgD+AUGSRhzwGMAMZzg+4Fduqh7gS1WjLD+QCZwfk8Iu16q/LokbdB+rDm2JlqVOefqmQASDA+Md8BeD43EPXcvCbb0vL1ffFnFSeoXQrskZkQLpxK3k1GnF39Kin4Y0kp24FJ+DIEL6QgX/vu1bzXaS99tL7eNwtTxt1tPJsrl9TVr7SkVwHUPDGtWZirQYl4QRrkZG/QB/GkUJ6kJZns8IbdOYed7AjqyL7l4AtMY9P3TEwFjIzQRnVEXNOTnz515YgU/gfq/WXxmyTNuxfUU4+8bnBj0npx1lBOSfPDtX1bZ4VAWk9/S9z9RU/lN4HA==; csrf_token=85138258-b33e-4ed1-87b5-9a270aa615a7',
}


def returnReviewsList(code, reviews_count = 10):
    reviews_list = list()
    for i in range(1, reviews_count + 1):
        params = (
            ('code', code),
            ('type', 'after'),
            ('isActualPointWriteExecute', 'false'),
            ('isMileageSubscriptionAlready', 'false'),
            ('isMileageSubscriptionReject', 'false'),
            ('page', i)
        )
        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')
        reviews = soup.select('.score_result > ul > li')
        count = 0
        for review in reviews:    
            star_rating = review.select_one('.star_score > em').text
            comment_html = review.select_one(f'.score_reple > p > span#_filtered_ment_{count}')
            comment = comment_html.text
            if comment_html.select_one('span._unfold_ment'):
                comment = comment_html.select_one('._unfold_ment > a')['data-src']
            reviews_list.append({
              'star': star_rating,
              'comment': comment.strip()
            })
            count += 1
    return reviews_list


    
