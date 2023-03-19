import requests
import re

url = "http://natas0.natas.labs.overthewire.org/"
user = "natas0"
password = "natas0"

r = requests.get(url, auth=(user, password))
comments = re.findall(r'<!--(.*?)-->', r.text, re.DOTALL)

for comment in comments:
    if "password" not in comment:
        continue
    print(f"Natas0:{comment.split()[-1]}")
