import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
movies = list()
movie_a_tags = soup.select('.lst_dsc > .tit > a')

for tag in movie_a_tags:
    movie_info = {
      'title': tag.text,
      'code': tag['href'].split('?code=')[1]
    }
    print(movie_info)
    movies.append(movie_info)

