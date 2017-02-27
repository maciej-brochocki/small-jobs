#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import images
from db_scheme import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		student = db.get(db.Key.from_path('Student', int(self.request.get('id'))))
		if student:
			if student.avatar:
				self.response.headers['Content-Type'] = "image/png"
				self.response.out.write(student.avatar)
			else:
				if student.type == 1:
					self.redirect('gfx/user_student.png')
				else:
					self.redirect('gfx/user_company.png')
		else:
			self.response.out.write("No user")

def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
