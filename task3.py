import json
import pprint
file =  open("by_year.json","r")
read = file.read()
data = json.loads(read)
dict1 = {}
for i in data :
    list1= []
    a = str(i)
    for j in data :
        b = str(j)
        if a[:3] == b[:3]:
            k = 0
            while k < len(data[j]):
                if data[j][k] not in list1:
                    list1.append(data[j][k])
                k+=1
    b = a[:3]+"0"
    dict1[int(b)] = list1
with open("by_decade.json","w") as f:
    json.dump(dict1,f,indent=4)