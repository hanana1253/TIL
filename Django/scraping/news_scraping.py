import requests
from bs4 import BeautifulSoup

for startnum in range(1, 100, 10):
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98&start={}'.format(startnum)
    response = requests.get(url)
    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')
    news_headings = soup.find_all("a", "news_tit")
    for heading in news_headings:
        print(heading['title'], heading['href'], sep='\n')
