#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from db_scheme import *
from logged import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		id = self.request.get('id')
		if not id:
			#Zle wolanie
			msg = 1
		else:
			try:
				student = db.get(db.Key(id))
				if student.active:
					#Juz aktywny
					msg = 3
				else:
					if self.request.get('del'):
						#Usuniecie
						student.delete()
						msg = 4
					else:
						#Aktywacja
						student.active = True
						student.put()
						msg = 5
			except:
				#Brak rekordu
				msg = 2
		values = {'msg': msg}
		values.update(logged())
		self.response.out.write(template.render('student_activate.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
