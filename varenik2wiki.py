#!/usr/bin/python3

import pywikibot
import json
import pprint
from urllib.request import urlopen

# site = pywikibot.Site()
# page = pywikibot.Page(site, u"Varenik json")
# text = page.text 

# print("Argument List: %s!" % str(sys.argv))

with urlopen('https://opensheet.elk.sh/1lWvfxzdlWNxWuWCW1rRWy4TON-XIuE4jOmlJmq5SYNA/%D0%9A%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F') as resp:
  project_info = json.load(resp)

pprint.pprint(project_info)
# page.save(u"Bot insert")


