#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from db_scheme import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		voivodeship = Voivodeship(name=u'cała Polska')
		voivodeship.put()
		city = City(voivodeship=voivodeship.key(), name=u'praca zdalna', people=100)
		city.put()
		category = Category(name=u'grafika, fotografia, wideo')
		category.put()
		category = Category(name=u'korepetycje')
		category.put()
		category = Category(name=u'marketing i sprzedaż')
		category.put()
		category = Category(name=u'montaż i naprawa')
		category.put()
		category = Category(name=u'odbiór i dostawa')
		category.put()
		category = Category(name=u'odśnieżanie')
		category.put()
		category = Category(name=u'opieka nad dziećmi')
		category.put()
		category = Category(name=u'opieka nad osobą niepełnosprawną')
		category.put()
		category = Category(name=u'opieka nad seniorem')
		category.put()
		category = Category(name=u'opieka nad zwierzętami')
		category.put()
		category = Category(name=u'organizacja imprez')
		category.put()
		category = Category(name=u'pomoc dla firm')
		category.put()
		category = Category(name=u'pomoc z komputerem')
		category.put()
		category = Category(name=u'programowanie')
		category.put()
		category = Category(name=u'przenoszenie ciężkich rzeczy')
		category.put()
		category = Category(name=u'prace biurowe')
		category.put()
		category = Category(name=u'prace domowe')
		category.put()
		category = Category(name=u'prace ogrodowe')
		category.put()
		category = Category(name=u'prace remontowe')
		category.put()
		category = Category(name=u'prace twórcze')
		category.put()
		category = Category(name=u'prace wirtualne')
		category.put()
		category = Category(name=u'sprzątanie')
		category.put()
		category = Category(name=u'zakupy')
		category.put()
		category = Category(name=u'...inne zadania')
		category.put()

		self.response.out.write(template.render('fill_db.html', {}))
	
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
