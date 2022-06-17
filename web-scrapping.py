import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint

base_url = 'https://habr.com'
url = base_url + '/ru/all'
KEYWORDS = ['дизайн', 'фото', 'web', 'Python']

HEADERS = {'Accept': '*/*',
 'Connection': 'keep-alive',
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
               'like Gecko) Chrome/71.0.3578.80 Safari/537.36 '
               'OPR/56.0.3051.104'}



res = requests.get(url, headers=HEADERS)
text = res.text
soup = BeautifulSoup(text, features="html.parser")


articles = soup.find_all('article')
for article in articles:
    previews = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
    previews = [preview.text.strip() for preview in previews]

    for preview in previews:
        if KEYWORDS in previews:
            links = article.find(class_="tm-article-snippet__title-link").attrs['href']
            pprint(f'{preview} -------- {base_url}{links}')

