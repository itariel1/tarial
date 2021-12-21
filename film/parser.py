import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

# HOST = "https://animekisa.tv/"
# URL = "https://animekisa.tv/latest/1"

HOST_2 = "https://kinogo.biz/"
URL_2 = "https://kinogo.biz/new/"

# HEADERS = {"
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
# }

HEADERS_2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.910 Yowser/2.5 Safari/537.36',
}

# @csrf_exempt
# def get_html(url, params=''):
#     req = requests.get(url, headers=HEADERS, params=params)
#     return req

@csrf_exempt
def get_html_2(url_2, params=''):
    req_2 = requests.get(url_2, headers=HEADERS_2, params=params)
    return req_2

# @csrf_exempt
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='episode-box test')
#     anime = []
#
#     for item in items:
#         anime.append(
#             {
#                 'title': item.find('div', class_='title-box-2').get_text(strip=True),
#                 'image': HOST + item.find('div', class_='image-box').find('img').get('src')
#             }
#         )
#     print(anime)
#     return anime

# @csrf_exempt
# def anime_parser():
#     html = get_html(URL)
#     if html.status_code == 200:
#         anime = []
#         for page in range(0,1):
#             html = get_html(URL, params={'page':page})
#             anime.extend(get_content(html.text))
#             return anime
#     else:
#         raise ValueError('Error in ANIME PARSER')

@csrf_exempt
def get_content_2(html):
     soup = BeautifulSoup(html, 'html.parser')
     items = soup.find_all('div', class_='shortstory')
     movie = []

     for item in items:
        movie.append(
            {
                'title': item.find('h2', class_='zagolovki').get_text(strip=True),
                'image': HOST_2 + item.find('img').get('src')
            }
         )
     print(movie)
     return movie

@csrf_exempt
def movie_parser():
    html = get_html_2(URL_2)
    if html.status_code == 200:
        movie = []
        for page in range(0,2):
            html = get_html_2(URL_2, params={'page':page})
            movie.extend(get_content_2(html.text))
            return movie
    else:
        raise ValueError('Error in MOVIE PARSER')