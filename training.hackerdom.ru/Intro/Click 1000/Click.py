#!/usr/bin/python
# -*- coding: utf-8 -*-

import lxml.html as html
import argparse
from urlparse import urljoin


# http://click1000.training.hackerdom.ru/
items = 1
BASE_URL = "http://click1000.training.hackerdom.ru/"
hash = '467c0cf0a7f70cd6fb3999e38cdfae69'
for item in range(0, items+1):
	url = BASE_URL + hash
	page = html.parse(url)
	print(page)

	hash = page[8:41]
	print(hash)
	outputFile = open ('tmp/item-{}.log'.format(item), 'w') # for log
	outputFile.write(page)
	outputFile.close()
	#progress(item)

print ("FIN")