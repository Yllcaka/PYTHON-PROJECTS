#! /usr/bin/python3
import requests,sys
address = "".join(sys.argv[1])
res = requests.get(address)
print(res.status_code)
# print(len(res.text))
print(res.text[:int(sys.argv[2])])
with open("Site.txt","wb") as site:
    for chunk in res.iter_content(100000):
        site.write(chunk)