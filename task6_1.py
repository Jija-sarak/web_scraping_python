import json
f = open("top_10_movie_details.json","r")
read = f.read()
data = json.loads(read)
i = 0
count_of_language = {}
while i < len(data):
    j = 0
    count = 0 
    while j < len(data[i]["language"]):
        count = 0
        k = 0 
        while k < len(data):
            for l in data[k]["language"]:
                if  data[i]["language"][j] == l :
                    count+=1
            k+=1
        count_of_language[data[i]["language"]] = count
        j+=1
    i+=1
print(count_of_language)
# import requests
# from bs4 import BeautifulSoup
# import json
# import pprint
# f = open("top_movies.json","r")
# read = f.read()
# data = json.loads(read)
# movie_details_list = []
# i = 0
# while i < 10:
#         def scrape_movie_details(movie_url):
#             page = requests.get(movie_url)
#             soup = BeautifulSoup(page.text,'html.parser')
#             poster = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
#             poster = soup.find('div',class_ = "col mob col-center-right col-full-xs mop-main-column")
#             poster_image = poster.find('button',class_ = "trailer_play_action_button")
#             if poster_image is None:
#                 poster_image = poster.find('div',class_="movie-thumbnail-wrap").img
#                 image = poster_image["data-src"]
#             else:
#                 image = poster_image["data-thumbnail"]
        
#             movie_name = poster.find('div',class_ = "thumbnail-scoreboard-wrap").h1.get_text()

#             movie_info = poster.find('section',class_ = "panel panel-rt panel-box movie_info media")
#             info = movie_info.find('div',class_ = "panel-body content_body")
#             bio = info.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
            
#             movie_genre = info.find('ul',class_="content-meta info")
#             genre = movie_genre.find('div',class_= "meta-value genre").get_text()
#             list1=[]
#             sum = ""
#             for i in genre:
#                 if "," not in genre :
#                     list1.append(genre.strip())
#                     break
#                 if i != ",":
#                     if i.isalpha():
#                         sum+=i
#                 else:
#                     list1.append(sum)
#                     sum = ""
#             movie_genre = info.find('ul',class_="content-meta info")
#             sub_li = movie_genre.find_all('li')
#             for li in sub_li:
#                 sub = li.find('div',class_="meta-label subtle").get_text().strip()
#                 if sub == "Original Language:" :
#                     lan = li.find('div',class_ = "meta-value").get_text().strip()
#                 if sub == "Director:" :
#                     direct = li.find("div",class_ = "meta-value")
#                     director = direct.find_all('a')
#                     list3 = []
#                     for a in director :
#                         list3.append(a.get_text())
#                 if sub == "Runtime:":
#                     duration = li.find("div",class_="meta-value").get_text().strip()
#                     if len(duration) == 5:
#                         runtime = int(duration[0])*60+int(duration[3:4])
#                     else:
#                         runtime = int(duration[0])*60+int(duration[3:5])
                    
#             dict1 = {"name":"","Director":"" , "language":"", "poster_image_url":"","bio":"", "runtime":"","genre":""}
#             dict1["name"] = movie_name
#             dict1["poster_image_url"] = image
#             dict1["bio"] = bio
#             dict1["genre"] = list1
#             dict1["language"] = lan
#             dict1["Director"] = list3
#             dict1["runtime"] = runtime
#             movie_details_list.append(dict1)
#         url1 = data[i]["url"]
#         scrape_movie_details(url1)
#         i+=1
# i = 0
# count_of_language = {}
# while i < len(movie_details_list):
#         count = 0
#         k = 0 
#         while k < len(movie_details_list):
#             if  movie_details_list[i]["language"] == movie_details_list[k]["language"] :
#                     count+=1
#             k+=1
#         count_of_language[movie_details_list[i]["language"]] = count
#         i+=1
# print(count_of_language)
