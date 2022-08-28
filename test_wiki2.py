# /usr/bin/python3

import pywikibot
import sys

print("Argument List: %s!" % str(sys.argv))

site = pywikibot.Site()
page = pywikibot.Page(site, u"Тестирую_wikibot_APIs")
text = page.text 

args_text = ' '.join(sys.argv[1:])
print("args_text: %s" % str(args_text))

page.text = text + "<br>new text: " + str(args_text)

# u"newText!"
page.save(u"Edit comment")


