import json
import pprint
f = open("top_10_movie_details.json","r")
read = f.read()
data = json.loads(read)
i = 0
count_of_directors = {}
while i < len(data):
    j = 0 
    while j < len(data[i]["Director"]):
        count = 0
        k = 0 
        while k < len(data):
            for l in data[k]["Director"]:
                if  data[i]["Director"][j] == l :
                    count+=1
            k+=1
        count_of_directors[data[i]["Director"][j]] = count
        j+=1
    i+=1
print(count_of_directors)
#     for k in data[i]["Director"]:
#         j = 0
#         c = 0
#         sum = ""
#         while j< len(data):
#             if k in data[j]["Director"]:
#                 c+=1
#                 sum = k
#             j+=1
#         count_of_directors[sum] =  c
#     i+=1
# pprint.pprint(count_of_directors)