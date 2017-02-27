#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from pyipinfodb import IPInfo
from db_scheme import *
from sets import Set
from sessions import *
from logged import *

class MainHandler(webapp.RequestHandler):
	def default_form(self, new_values):
		ipinfo = IPInfo('please_enter_valid')
		geo = ipinfo.GetCity(self.request.remote_addr)
#		geo = ipinfo.GetCity('81.190.71.212') #Gdynia for localhost testing
		cities = db.GqlQuery("SELECT * FROM City WHERE name=:name LIMIT 1", name = geo['City'])
		if cities.count() == 0:
			cities = db.GqlQuery("SELECT * FROM City WHERE name=:name LIMIT 1", name = 'Warszawa')
		city = cities.fetch(1,0)[0]
		miasto = city.name
		wojewodztwo = city.voivodeship.name
		miasta = city.voivodeship.city_set.order("-people")
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa,
			'rules': 1, 'data': 1, 'spam': 1}
		values.update(new_values)
		values.update(logged())
		self.response.out.write(template.render('student_login.html', values))
		
	def get(self):
		self.default_form({'errors': Set()})
	
	def post(self):
		errors = Set()

		if self.request.get('form') == "1":
			#Login
			students = db.GqlQuery("SELECT * FROM Student WHERE email=:email LIMIT 1", email = self.request.get('log_email'))
			if students.count() == 0:
				errors.add('e_log_email')
			else:
				student = students.fetch(1,0)[0]
				if not student.password == self.request.get('log_password'):
					errors.add('e_log_password')
				else:
					if student.active == 0:
						errors.add('e_not_active')
			if len(errors) == 0:
				session = Session()
				session['student_id'] = student.key().id()
				try:
					self.redirect(session['after_student_login'])
				except:
					self.redirect('/')
				return
			else:
				values = {'log_email': self.request.get('log_email'), 'errors': errors}
				self.default_form(values)
				return

		if self.request.get('form') == "3":
			#Voivodeship change
			voivodeships = db.GqlQuery("SELECT * FROM Voivodeship WHERE name=:name LIMIT 1", name = self.request.get('voivodeship'))
			voivodeship = voivodeships.fetch(1,0)[0]
			wojewodztwo = voivodeship.name
			miasta = voivodeship.city_set.order("-people")
			miasto = miasta.fetch(1,0)[0].name
			wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")
			values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa,
				'type': self.request.get('type'), 'nick': self.request.get('nick'), 'name': self.request.get('name'),
				'phone': self.request.get('phone'), 'email': self.request.get('email'), 'age': self.request.get('age'),
				'rules': self.request.get('rules'), 'data': self.request.get('data'), 'spam': self.request.get('spam'),
				'errors': Set()}
			values.update(logged())
			self.response.out.write(template.render('student_login.html', values))
			return
		
		#Register
		nick = self.request.get('nick').strip().lower()
		email = self.request.get('email').strip().lower()
		if not nick:
			errors.add('e_no_nick')
		else:
			#Nazwa profilu zajeta
			students = db.GqlQuery("SELECT * FROM Student WHERE nick=:nick LIMIT 1", nick = nick)
			if students.count() == 1:
				errors.add('e_nick')
		if not self.request.get('name'):
			errors.add('e_no_name')
		if not self.request.get('phone'):
			errors.add('e_no_phone')
		if not self.request.get('email'):
			errors.add('e_no_email')
		else:
			#Email juz uzyty
			students = db.GqlQuery("SELECT * FROM Student WHERE email=:email LIMIT 1", email = email)
			if students.count() == 1:
				errors.add('e_email')
		if not self.request.get('password'):
			errors.add('e_no_password')
		else:
			#Haslo sie nie zgadza
			if not self.request.get('password') == self.request.get('password2'):
				errors.add('e_password')
		#Musisz spelniac warunki
		if not self.request.get('age'):
			errors.add('e_age')
		#Musisz zaakceptowac regulamin
		if not self.request.get('rules'):
			errors.add('e_rules')
		#Musisz zezwolic na przetwarzanie danych
		if not self.request.get('data'):
			errors.add('e_data')

		cities = db.GqlQuery("SELECT * FROM City WHERE name=:name LIMIT 1", name = self.request.get('city'))
		city = cities.fetch(1,0)[0]
			
		if len(errors) == 0:
			student = Student(type = int(self.request.get('type')), nick = nick, name = self.request.get('name'),
				phone = self.request.get('phone'), email = email, password = self.request.get('password'),
				spam = self.request.get('spam')=='on', active = False, city = city, notify = 1)
			student.put()
			message = template.render('student_confirm.txt', {'name': self.request.get('nick'), 'id': student.key()})
			mail.send_mail(sender="SzybkaFucha.pl <admin@szybkafucha.pl>",
				to=self.request.get('email'),
				subject="Potwierdzenie rejestracji",
				body=message)
			self.redirect('student_confirm.html') 
			return

		miasto = city.name
		wojewodztwo = city.voivodeship.name
		miasta = city.voivodeship.city_set.order("-people")
		wojewodztwa = db.GqlQuery("SELECT * FROM Voivodeship ORDER BY name")
		values = {'miasto': miasto, 'wojewodztwo': wojewodztwo, 'miasta': miasta, 'wojewodztwa': wojewodztwa,
			'type': self.request.get('type'), 'nick': nick, 'name': self.request.get('name'),
			'phone': self.request.get('phone'), 'email': email, 'age': self.request.get('age'),
			'rules': self.request.get('rules'), 'data': self.request.get('data'), 'spam': self.request.get('spam'),
			'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('student_login.html', values))
	
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
