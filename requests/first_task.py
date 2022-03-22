import requests
from pprint import pprint

url = "https://superheroapi.com/api/2619421814940190/655/powerstats" # Thanos
url1 = "https://superheroapi.com/api/2619421814940190/149/powerstats" # Captain America
url2 = "https://superheroapi.com/api/2619421814940190/332/powerstats" # Hulk
r = requests.get(url)
r1 = requests.get(url1)
r2 = requests.get(url2)



i1 = r.json()['intelligence']
n1 = r.json()['name']
i2 = r1.json()['intelligence']
n2 = r1.json()['name']
i3 = r2.json()['intelligence']
n3 = r2.json()['name']
dct = {n1: int(i1), n2: int(i2), n3: int(i3)}
print(dct)
max_val = max(dct.values())
final_dict = {k: v for k, v in dct.items() if v == max_val}
for key in final_dict:
    print(f"The smartest is: {key}")

