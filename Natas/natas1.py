import requests
import re

url = "http://natas1.natas.labs.overthewire.org/"
user = "natas1"
password = "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"

r = requests.get(url, auth=(user, password))
comments = re.findall(r'<!--(.*?)-->', r.text, re.DOTALL)

for comment in comments:
    if "password" not in comment:
        continue
    print(f"Natas1:{comment.split()[-1]}")
