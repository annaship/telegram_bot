#!/usr/bin/python3

import pywikibot
import json
import pprint
#from urllib.request import urlopen
import urllib

# site = pywikibot.Site()
# page = pywikibot.Page(site, u"Varenik json")
# text = page.text 

# print("Argument List: %s!" % str(sys.argv))

varenik_json_url = 'https://opensheet.elk.sh/1lWvfxzdlWNxWuWCW1rRWy4TON-XIuE4jOmlJmq5SYNA/%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F'
str_enc = varenik_json_url.encode('utf-8')

from socket import timeout
try:
    response = urllib.request.urlopen(str_enc, timeout=10).read().decode('utf-8')
#except HTTPError as error:
#    logging.error('HTTP Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
#except URLError as error:
#    if isinstance(error.reason, timeout):
#        logging.error('Timeout Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
except Exception as inst:
        print('Error:  %s not retrieved \nURL: %s', inst, str_enc)
    #else:
        #logging.error('URL Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
else:
    print('Access successful.')

#with urlopen(str_enc) as resp:
#  project_info = json.load(resp)

#with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
#    project_info = json.load(resp)['info']

#pprint.pprint(response)
# page.save(u"Bot insert")



