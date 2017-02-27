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
		student = log_student()
		if not student:
			session = Session()
			session['after_student_login'] = 'student_profile.html'
			self.redirect('student_login.html')
			return
		categories = db.GqlQuery("SELECT * FROM Category ORDER BY name")
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")

		errors = Set()
		miasta = student.city.voivodeship.city_set.order("-people")

		miasto = student.city.name
		wojewodztwo = student.city.voivodeship.name
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa, 'categories': categories, 'student': student, 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('student_profile.html', values))
	
	def post(self):
		student = log_student()
		if not student:
			session = Session()
			session['after_student_login'] = 'student_profile.html'
			self.redirect('student_login.html')
			return
		categories = db.GqlQuery("SELECT * FROM Category ORDER BY name")
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")

		if self.request.get('form') == "2":
			#Voivodeship change
			voivodeships = db.GqlQuery("SELECT * FROM Voivodeship WHERE name=:name LIMIT 1", name = self.request.get('voivodeship'))
			voivodeship = voivodeships.fetch(1,0)[0]
			miasta = voivodeship.city_set.order("-people")
			student.city = miasta.fetch(1,0)[0]
		else:
			cities = db.GqlQuery("SELECT * FROM City WHERE name=:name LIMIT 1", name = self.request.get('city'))
			student.city = cities.fetch(1,0)[0]
			miasta = student.city.voivodeship.city_set.order("-people")
		
		errors = Set()
		student.type = int(self.request.get('type'))
		if not self.request.get('name'):
			errors.add('e_no_name')
		else:
			student.name = self.request.get('name')
		if not self.request.get('phone'):
			errors.add('e_no_phone')
		else:
			student.phone = self.request.get('phone')
		if self.request.get('old_password'):
			if not student.password == self.request.get('old_password'):
				errors.add('e_old_password')
			else:
				if not self.request.get('password'):
					errors.add('e_no_password')
				else:
					#Haslo sie nie zgadza
					if not self.request.get('password') == self.request.get('password2'):
						errors.add('e_password')
					else:
						student.password = self.request.get('password')
		student.spam = self.request.get('spam')=='on'

		if self.request.get("pic"):
			avatar = images.resize(self.request.get("pic"), 64, 64)
			student.avatar = db.Blob(avatar)
		categories_sel = []
		for category in categories:
			if self.request.get('%d' % category.key().id()):
				categories_sel.append(category.key())
		student.specialities = categories_sel
		student.description = self.request.get("description")
		student.notify = int(self.request.get('notify'))
		if self.request.get('form') == "1":
			student.put()

		miasto = student.city.name
		wojewodztwo = student.city.voivodeship.name
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa, 'categories': categories, 'student': student, 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('student_profile.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
