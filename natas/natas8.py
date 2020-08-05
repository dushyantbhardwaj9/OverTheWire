#!/usr/bin/env python

import requests
import re
print("Natas Level 8")


username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

data = { "secret":"oubWYf2kBq","submit":"submit"}

url = "http://%s.natas.labs.overthewire.org/"%(username)

with requests.session() as session:
	response = session.post(url , auth = (username, password),data = data )

	content = response.text 

	# print( content)

	print( re.findall("Access granted. The password for natas9 is (.*)", content)[0] )

