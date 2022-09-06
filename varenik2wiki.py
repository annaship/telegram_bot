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

#__main__

data = get_varenik_json()
print(data)


# site = pywikibot.Site()
# page = pywikibot.Page(site, u"Varenik json")
# text = page.text 

# print("Argument List: %s!" % str(sys.argv))

# page.save(u"Bot insert")



