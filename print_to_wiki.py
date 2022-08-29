#!/usr/bin/python3

import pywikibot
import sys
import base64

print("Argument List: %s!" % str(sys.argv))

site = pywikibot.Site()
page = pywikibot.Page(site, u"Ссылки_из_Телеграма_на_разбор")
text = page.text 

args_text = ' '.join(sys.argv[1:])
args_text = args_text.replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>")
print("args_text: %s" % str(args_text))

page.text = text + "<br>new text: " + str(args_text)

# u"newText!"
page.save(u"Edit comment")


