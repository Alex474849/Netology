import requests
from pprint import pprint

url = "https://api.stackexchange.com/2.3/questions?todate=1648080000&order=desc&sort=activity&tagged=Python&site=stackoverflow"
r = requests.get(url)
pprint(r.json())