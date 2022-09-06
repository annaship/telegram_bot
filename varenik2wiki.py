#!/usr/bin/python3

import pywikibot
import json
import pprint
#from urllib.request import urlopen

from urllib import parse
from urllib import request

varenik_json_url = 'https://opensheet.elk.sh/1lWvfxzdlWNxWuWCW1rRWy4TON-XIuE4jOmlJmq5SYNA/%D0%9F    %D0%BE%D0%BB%D0%BD%D0%B0%D1%8F'

parts = parse.urlsplit(varenik_json_url)
query_dict = parse.parse_qs(parts.query)
encoded_query = parse.urlencode(query_dict)
fixed_url = parse.urlunsplit((parts.scheme, parts.netloc, parts.path, encoded_query, parts.fragment))
response = request.urlopen(fixed_url)

print(json.load(response))

# site = pywikibot.Site()
# page = pywikibot.Page(site, u"Varenik json")
# text = page.text 

# print("Argument List: %s!" % str(sys.argv))

# page.save(u"Bot insert")



