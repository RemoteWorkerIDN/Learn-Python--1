users = {"id": 1,
         "name": "Leanne Graham",
         "username": "Bret",
         "email": "Sincere@april.biz",
         "address": {
             "street": "Kulas Light",
             "suite": "Apt. 556",
             "city": "Gwenborough",
             "zipcode": "92998-3874",
             "geo": {
                 "lat": "-37.3159",
                 "lng": "81.1496"
             }}}
print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["email"])
print(users["address"])
print(users["address"]["geo"]["lat"])

"""
Cara merubah dictionary menjadi JSON
"""
# untuk merubah dict menjadi json harus import package JSON yang ada pada python
print(users)

print("\nUbah dict ke JSON")
# hasil dari json.dumps adalah string
import json
#result = json.dumps(users)
#print(result)

result = json.dump
print((type)(result))
print(result)

with open("result.json","w") as file:
    json.dump(users, file)

