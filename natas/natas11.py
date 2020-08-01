#!/usr/bin/env python

import requests
import re
import urllib
import base64
import pwn
import itertools


username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

# data = { "needle":". /etc/natas_webpass/natas11 #","submit":"submit"}

url = "http://%s.natas.labs.overthewire.org/"%(username)
# print(url)
with requests.session() as session:
	response = session.get(url , auth = (username, password) )

	cipher = base64.b64decode(urllib.parse.unquote( response.cookies['data'] )).decode('utf-8')
	plain_text = str({ "showpassword" : "yes", "bgcolor": "#ffffff" })

	key = "qw8J"

	datsd = ''
	for i,j in zip(itertools.cycle(key),cipher):
		datsd += chr( ord(i)^ord(j) ) 
	print(datsd)

'''
plain_text = str({ "showpassword" : "no", "bgcolor": "#ffffff" })


cipher = str(base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="))

print(len(cipher), len(plain_text))

for i,j in zip(plain_text, cipher):
	print( chr( ord(i)^ord(j) ) )

'''

# key = pwn.xor(plain_text,cipher)
# print(key)

	# print(cipher)