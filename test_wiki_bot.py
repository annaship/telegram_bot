# /usr/bin/python3

import pywikibot
testwiki = pywikibot.Site()
testwiki
# APISite("ru", "rubikuswiki")
testwiki.login()
print('Logged in user is:', testwiki.user())
# Logged in user is: Ashipunova3


demo_page = pywikibot.Page(testwiki, '%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D1%83%D1%8E_wikibot_API')
# http://wikitest.rubikus.de/mediawiki/index.php?title=%D0%A2%D0%B5%D1%81%D1%82%D0%B8%D1%80%D1%83%D1%8E_wikibot_APIs&action=edit&redlink=1
demo_page
# Page('Тестирую wikibot API')
print(demo_page.text)

# pywikibot.exceptions.NoPageError: Page [[ru:Тестирую wikibot API]] doesn't exist.
demo_page = pywikibot.Page(testwiki, 'index.php/Тестирую_wikibot_APIs')

# pywikibot.exceptions.NoPageError: Page [[ru:Index.php/Тестирую wikibot APIs]] doesn't exist.

# demo_page = pywikibot.Page(testwiki, 'mediawiki/index.php/Тестирую_wikibot_APIs')
demo_page = pywikibot.Page(testwiki, 'User:Ashipunova3/Тестирую_wikibot_APIs')
# /home/rubikus/software/core_stable/pywikibot/page/_pages.py

# python pwb.py shell
# Welcome to the Pywikibot interactive shell!

site = pywikibot.Site()
site
# APISite("ru", "rubikuswiki")
page = pywikibot.Page(site, u"pageName")
page = pywikibot.Page(site, u"Заглавная_страница")
text = page.text
text
# 'Информацию по работе с этой вики можно найти в [https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents справочном руководстве].\n\nДля практики в редактировании<ref>[http://varenik.help]</ref> - [[тестовая страница]]<br>\n[[:Категория:Страны|Список всех стран]]<ref>Это категория</ref>\n== Начало работы ==\n* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Configuration_settings Список возможных настроек];\n* [https://www.mediawiki.org/wiki/Manual:FAQ/ru Часто задаваемые вопросы и ответы по MediaWiki];\n* [https://lists.wikimedia.org/postorius/lists/mediawiki-announce.lists.wikimedia.org/ Рассылка уведомлений о выходе новых версий MediaWiki].\n* [https://www.mediawiki.org/wiki/Special:MyLanguage/Localisation#Translation_resources Перевод MediaWiki на свой язык]\n* [https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Combating_spam Узнайте, как бороться со спамом в вашей вики]\n\n<references />'

page = pywikibot.Page(site, u"Тестирую_wikibot_APIs")
page.text = u"newText!"
page.save(u"Edit comment")
# Page [[Тестирую wikibot APIs]] saved

