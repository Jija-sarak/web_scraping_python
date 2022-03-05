import requests
from bs4 import BeautifulSoup
import json
import pprint
f = open("1top_movies.json","r")
read = f.read()
data = json.loads(read)
i = 0
zero = 0
while i < 10:
    def scrape_movie_details(movie_url):
        page = requests.get(movie_url)
        soup = BeautifulSoup(page.text,'html.parser')
                                            
        title_div = soup.find('div', class_ = "TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.get_text()
        
        time = soup.find('div',class_ = "TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
        l = time.find_all("li")
        for li in l :
            pass
        duration = li.get_text()
        if len(duration) == 5 :
            run = int(duration[0])*60+int(duration[3:4])
        else:
            run = int(duration[0])*60+int(duration[3:5])

        poster = soup.find('div', class_ = "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--base ipc-media--poster-s ipc-media__img").img['src']

        director = soup.find('div', class_ = "ipc-metadata-list-item__content-container").ul
        d = director.find_all("li")
        list1= []
        for li in d :
            list1.append(li.get_text())
        
        bio = soup.find('div' , class_ = "GenresAndPlot__ContentParent-sc-cum89p-8 hTqGWn Hero__GenresAndPlotContainer-sc-kvkd64-11 iEHpKn")
        if bio != None:
            b = bio.find_all("span")
            for span in b :
                pass
            sn = span.get_text()
        else :
            bio = soup.find('div' , class_ = "GenresAndPlot__OffsetContentParent-sc-cum89p-9 knVRar Hero__GenresAndPlotContainer-sc-kvkd64-11 iEHpKn")
            b = bio.find_all("span")
            for span in b :
                pass
            sn = span.get_text()
        
        genre = soup.find('div',class_ ="ipc-chip-list GenresAndPlot__GenresChipList-sc-cum89p-4 cDpOeC")
        if genre != None :
            g = genre.find_all("a")
            list2= []
            for a in g :
                list2.append(a.get_text())
            
        else:
            genre = soup.find('div',class_ ="ipc-chip-list GenresAndPlot__OffsetChipList-sc-cum89p-5 dZdTje")
            g = genre.find_all("a")
            list2= []
            for a in g :
                list2.append(a.get_text())
        dict1 = {"name":"", "runtime":"", "poster_image_url":"","Director":"","bio":"","genre":"","country":""}
        dict1["name"] = title_div
        dict1["runtime"] = run
        dict1["poster_image_url"] = poster
        dict1["Director"] = list1
        dict1["bio"]  = sn
        dict1["genre"] = list2


        lan = soup.find('div',class_ = "BTFWrapper__MainColumnContent-sc-1g8jgrg-1 fKIzsM ipc-page-grid__item ipc-page-grid__item--span-2")
        l = lan.find_all("section")            
        i = 0
        for section in l :
            if i == 8:                         
                a = section.find('div',class_ = "styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf")
                if a != None :
                    j = a.find_all("ul")
                    k = 1
                    for ul in j :
                        if k == 5 :
                            org = ul.find_all("li")
                            list3 = []
                            for li in org :
                                h = li.get_text()
                                list3.append(h)
                        k+=1
                else:
                    i = 0
                    for section in l :
                     if i == 10:                         
                        a = section.find('div',class_ = "styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf")
                        if a != None :
                            j = a.find_all("ul")
                            k = 1
                            for ul in j :
                                if k == 5 :
                                    org = ul.find_all("li")
                                    list3 = []
                                    for li in org :
                                        h = li.get_text()
                                        list3.append(h)
                                k+=1
                     if i == 10:                          
                            a = section.find('div',class_ = "styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf").ul
                            j = a.find_all("li")
                            k = 1
                            for li in j :   
                                if k == 4:
                                    country1 = li.get_text()
                                    print(zero+1,country1)
                                    dict1["country"] = country1
                                k+=1
                     i+=1     
            if i == 8:                          
                a = section.find('div',class_ = "styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf").ul
                j = a.find_all("li")
                k = 1
                for li in j :   
                    if k == 4:
                        country1 = li.get_text()
                        print(zero+1,country1)
                        dict1["country"] = country1
                    k+=1
            i+=1
        pprint.pprint(dict1)
    url1 = data[i]["url"]
    scrape_movie_details(url1)
    i+=1
    zero+=1

