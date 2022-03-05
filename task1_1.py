import json
import pprint
from bs4 import BeautifulSoup
import requests
url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
movie_ranks = []
movie_name = []
movie_url= []
movie_year = []
movie_rating = []
def top_scrap_list():
    main_div = soup.find('div',class_ = "panel-body content_body allow-overflow")
    sub_div = main_div.find('table',class_ = "table")
    trs = sub_div.find_all("td",class_="bold")
    for td in trs :
        a = td.get_text()
        movie_ranks.append(a)
    name = sub_div.find_all('a',class_ = "unstyled articleLink")
    for a in name :
        b = a.get_text()
        c = a["href"]
        d = "https://www.rottentomatoes.com"+c
        movie_url.append(d)
        movie_name.append(b[:-6])
        movie_year.append(b[-5:-1])
    rate = sub_div.find_all('span',class_ = "tMeterScore")
    for span in rate :
        g = span.get_text()
        movie_rating.append(g[1:])
    top_movies = []
    details = {'position':'','name':'','year':'','rating':'','url':''}

    for i in range(0,len(movie_ranks)):
        movie_ranks[i]= movie_ranks[i][:-1]
        details['position'] = int(movie_ranks[i])
        details['name'] = str(movie_name[i][12:].strip("\n"))
        details['year'] = int(movie_year[i])
        details['rating'] = movie_rating[i]
        details['url'] = movie_url[i]
        top_movies.append(details.copy())
    with open ("top_movies.json","w") as f:
        json.dump(top_movies , f , indent=4)
    return top_movies
pprint.pprint(top_scrap_list())