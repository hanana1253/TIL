import requests
from bs4 import BeautifulSoup
import json

# 영화 코드를 키로 하고, 정보 딕셔너리를 밸류로 하는 딕셔너리 생성
movie_infos = {}

# 1~7위 영화들은 따로 작업해서 movie_infos에 담아준다.
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}

response = requests.get('http://www.cgv.co.kr/movies/', headers=headers, verify=False)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
movies = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div.box-contents > a')

for movie in movies:
    code = movie['href'].split('?midx=')[1].strip()
    title = movie.text.strip()
    movie_infos[code] = { 'code': code, 'title': title }

# 더보기 이후에 있는 영화들의 코드와 제목을 json 파일로 가져와 movie_infos에 넣어주기
cookies = {
    'WMONID': 'QpWivmPWf6-',
    '_ga': 'GA1.3.1692882451.1617892584',
    'ASP.NET_SessionId': 'jbhk0esltxsv2tsain3ojez1',
    '_gid': 'GA1.3.481524181.1618893982',
    'CgvPopAd-': '',
    'CgvPopAd-movies': '%uA250%uA253%uA25B%uA24F%uA24C%uA25B',
    '_gat_UA-47951671-5': '1',
    '_gat_UA-47951671-7': '1',
    '_gat_UA-47126437-1': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'http://www.cgv.co.kr/movies/',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
}

params = (
    ('listType', '1'),
    ('orderType', '1'),
    ('filterType', '1'),
    ('_', '1618894150125'),
)

response = requests.get('http://www.cgv.co.kr/common/ajax/movies.aspx/GetMovieMoreList', headers=headers, params=params, cookies=cookies, verify=False)
more_movies = json.loads(response.text)
movie_dicts = json.loads(more_movies['d'])['List']
for movie_dict in movie_dicts:
    code = movie_dict['MovieIdx']
    title = movie_dict['Title']
    movie_infos[code] = { 'code': code, 'title': title }


# 각 영화의 리뷰를 movie_infos의 각 영화에 넣어주기
def addReviewInfos(movie_code, review_num, data_dict):      
    cookies = {
        'WMONID': 'QpWivmPWf6-',
        '_ga': 'GA1.3.1692882451.1617892584',
        'ASP.NET_SessionId': 'jbhk0esltxsv2tsain3ojez1',
        '_gid': 'GA1.3.481524181.1618893982',
        'CgvPopAd-': '',
        'CgvPopAd-movies': '%uA250%uA253%uA25B%uA24F%uA24C%uA25B',
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'http://www.cgv.co.kr',
        'Referer': 'http://www.cgv.co.kr/movies/detail-view/?midx=83917',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,la;q=0.5',
    }
    data = { 'movieIdx': movie_code, 'pageIndex': 1, 'pageSize': review_num, 'orderType': 0, 'filterType': 1, 'isTotalCount' : True, 'isMyPoint' : 'false' }

    response = requests.post('http://www.cgv.co.kr/common/ajax/point.aspx/GetMoviePointVariableList', headers=headers, cookies=cookies, json=data, verify=False)
    review_infos = json.loads(response.text)
    review_dicts = json.loads(review_infos['d'])['List']
    review_list = []
    for review_dict in review_dicts:
        egg = review_dict['EggPoint']
        comment = review_dict['CommentText']
        review_list.append({'egg': egg, 'comment':comment})
    data_dict[movie_code]['review'] = review_list

for movie_code in movie_infos:
    addReviewInfos(movie_code, 10, movie_infos)
