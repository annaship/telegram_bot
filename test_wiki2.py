# /usr/bin/python3

import pywikibot
import sys
print("Argument List: %s!" % str(sys.argv))

site = pywikibot.Site()
page = pywikibot.Page(site, u"Тестирую_wikibot_APIs")
text = page.text

args_text = ' '.join(sys.argv[1:])
page.text = text + "<br>new text: " + ' '.join(args_text)
# new text: F o r w a r d e d f r o m B o t F a t h e r


# u"newText!"
page.save(u"Edit comment")