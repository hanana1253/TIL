import json
import requests
from bs4 import BeautifulSoup


def soupReturn(url):
    res = requests.get(url)
    html_text = res.text
    return BeautifulSoup(html_text, 'html.parser')

def movieDataReturn():
    url = 'https://movie.naver.com/movie/running/premovie.nhn'
    soup = soupReturn(url)
    movie_list = soup.select('#content > div.article > div.obj_section > div.lst_wrap')

    data_list = list()
    for movie in movie_list:
        movie_a_list = movie.select('ul > li > dl > dt > a')
        for movie_a in movie_a_list:
            movie_data = {
                'title': movie_a.text,
                'code': movie_a['href'].split('?code=')[1]
            }
            data_list.append(movie_data)
    
    return data_list

movie_data_total = movieDataReturn()

def getStaffDataList(code):
    url = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={code}'
    soup = soupReturn(url)
    staff_data_list = list()
    staff_infos = soup.select('#content > div.article > div.section_group.section_group_frst > div > div.people > ul > li > a.tx_people')
    for info in staff_infos:
        staff_data_list.append(info.text)
    return staff_data_list

count = 0
for data in movie_data_total:
    code = data['code']
    movie_data_total[count]['staff'] = getStaffDataList(code)
    count += 1

data = {'movies': movie_data_total}

with open('movies.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

with open('movies.json', 'r', encoding='utf-8') as f:
    des_data = json.load(f)
