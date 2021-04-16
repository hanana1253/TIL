import requests
from bs4 import BeautifulSoup

news_data_total = list()

def soupMake(url):
    res = requests.get(url)
    html_text = res.text
    return BeautifulSoup(html_text, 'html.parser')

def newsScraping(soup):
    news_lis = soup.select('#main_pack > section > div > div.group_news > ul > li')
    count = 1
    for li in news_lis:
        a_tag = li.select_one('li > div.news_wrap > div > a')
        news_data = {
          'title': a_tag['title'], 
          'link': a_tag['href']
        }
        news_data_total.append(news_data)
        count += 1

for i in range(1, 101 + 1, 10):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%84%B8%EC%9B%94%ED%98%B8&start={i}'
    soup = soupMake(url)
    newsScraping(soup)

print(news_data_total[109])