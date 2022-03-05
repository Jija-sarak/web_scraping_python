import json
file = open("top_movies.json","r")
read = file.read()
data = json.loads(read)
i = 0
while i < len(data):
    j = 0
    while j < len(data):
        if data[i]["year"]< data[j]["year"]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        j+=1
    i+=1
dict1 = {}
i = 0
while i < len(data):
    list1 = []
    j = 0
    while j < len(data):
        if data[i]["year"] == data[j]["year"]:
            list1.append(data[j])
        j+=1
    dict1[data[i]["year"]] = list1
    i+=1
with open("by_year.json","w") as f:
    json.dump(dict1 , f , indent=4)



