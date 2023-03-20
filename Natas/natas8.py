import requests
import re
import binascii, base64

url = "http://natas8.natas.labs.overthewire.org/"
user = "natas8"
password = "a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB"
secret = "3d3d516343746d4d6d6c315669563362"

def decodeSecret(secret):
    decode = binascii.unhexlify(secret).decode()
    return base64.b64decode(decode[::-1]).decode()

decoded_secret = decodeSecret(secret)

data = {
    "secret":decoded_secret,
    "submit":"submit"
}

r = requests.post(url, auth=(user, password), data=data)

result = re.findall(r"The password for natas9 is (.*)", r.text)[0]

print(f"Natas9:{result}")
