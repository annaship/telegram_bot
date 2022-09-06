#!/usr/bin/python3

import pywikibot
import json
import pprint
#from urllib.request import urlopen

from urllib import parse
#from urllib import request
from urllib.request import Request, urlopen

def clean_url():
	varenik_json_url = 'https://opensheet.elk.sh/1lWvfxzdlWNxWuWCW1rRWy4TON-XIuE4jOmlJmq5SYNA/Kratkaya'
	parts = parse.urlsplit(varenik_json_url)
	query_dict = parse.parse_qs(parts.query)
	encoded_query = parse.urlencode(query_dict)
	fixed_url = parse.urlunsplit((parts.scheme, parts.netloc, parts.path, encoded_query, parts.fragment))
	return fixed_url

def get_varenik_json():
	req = Request(
		url=clean_url(), 
		headers={'User-Agent': 'Mozilla/5.0'}
	)
 
	webpage = urlopen(req).read()
 	#print(webpage.decode("UTF-8"))
	return webpage.decode("UTF-8")

def to_wiki(country, category, value):
	site = pywikibot.Site()
	page_name = "%s:%s" % (country, category)
	page = pywikibot.Page(site, page_name)
	old_text = page.text 
	new_text = value

	print("page_name = %s" % page_name)
	print("text: %s!" % str(new_text[:100]))

	# page.save(u"Bot insert")

#__main__

data = get_varenik_json()
#print(data)
#print("Type:", type(data))
j_data = json.loads(data)
#print("Type j_data:", type(j_data))

for i in j_data:
#	print("i = %s", i)
	for k, v in i.items():
		#print("k = %s, v = %s" % (k, v))
		if k == "Страна":
			country = v
		else:
			category = k
			value = v
			#print("country:category = %s:%s, value = %s" % (country, category, value[:100]))
			to_wiki(country, category, value)



