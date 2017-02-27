#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import images
from sets import Set
from logged import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		client = log_client()
		if not client:
			session = Session()
			session['after_client_login'] = 'client_profile.html'
			self.redirect('client_login.html')
			return
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")

		errors = Set()
		miasta = client.city.voivodeship.city_set.order("-people")

		miasto = client.city.name
		wojewodztwo = client.city.voivodeship.name
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa, 'client': client, 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('client_profile.html', values))
	
	def post(self):
		client = log_client()
		if not client:
			session = Session()
			session['after_client_login'] = 'client_profile.html'
			self.redirect('client_login.html')
			return
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")

		if self.request.get('form') == "2":
			#Voivodeship change
			voivodeships = db.GqlQuery("SELECT * FROM Voivodeship WHERE name=:name LIMIT 1", name = self.request.get('voivodeship'))
			voivodeship = voivodeships.fetch(1,0)[0]
			miasta = voivodeship.city_set.order("-people")
			client.city = miasta.fetch(1,0)[0]
		else:
			cities = db.GqlQuery("SELECT * FROM City WHERE name=:name LIMIT 1", name = self.request.get('city'))
			client.city = cities.fetch(1,0)[0]
			miasta = client.city.voivodeship.city_set.order("-people")
		
		errors = Set()
		client.type = int(self.request.get('type'))
		if not self.request.get('name'):
			errors.add('e_no_name')
		else:
			client.name = self.request.get('name')
		if not self.request.get('phone'):
			errors.add('e_no_phone')
		else:
			client.phone = self.request.get('phone')
		if self.request.get('old_password'):
			if not client.password == self.request.get('old_password'):
				errors.add('e_old_password')
			else:
				if not self.request.get('password'):
					errors.add('e_no_password')
				else:
					#Haslo sie nie zgadza
					if not self.request.get('password') == self.request.get('password2'):
						errors.add('e_password')
					else:
						client.password = self.request.get('password')
		client.spam = self.request.get('spam')=='on'

		client.notify = int(self.request.get('notify'))
		client.district = self.request.get('district')
		if self.request.get('form') == "1":
			client.put()

		miasto = client.city.name
		wojewodztwo = client.city.voivodeship.name
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa, 'client': client, 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('client_profile.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
