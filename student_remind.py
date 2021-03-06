﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from db_scheme import *
from sets import Set
from logged import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write(template.render('student_remind.html', logged()))
		
	def post(self):
		errors = Set()
		students = db.GqlQuery("SELECT * FROM Student WHERE email=:email LIMIT 1", email = self.request.get('email'))
		if students.count() == 0:
			errors.add('e_email')
		else:
			student = students.fetch(1,0)[0]
			message = template.render('student_remind.txt', {'name': student.nick, 'password': student.password})
			mail.send_mail(sender="SzybkaFucha.pl <admin@szybkafucha.pl>",
				to=self.request.get('email'),
				subject="Przypomnienie hasła",
				body=message)
			errors.add('c_sent')
		values = {'email': self.request.get('email'), 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('student_remind.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
