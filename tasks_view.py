#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from logged import *
from pytz_mini import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		student = log_student()
		if not student:
			session = Session()
			session['after_student_login'] = 'tasks_view.html'
			self.redirect('student_login.html')
			return
		
		tasks = db.GqlQuery("SELECT * FROM Task WHERE state = 1 ORDER BY time_added DESC LIMIT 100")
		dates_from = list()
		dates_to = list()
		utc = timezone('UTC')
		tz = timezone('Warsaw')
		for t in tasks:
			utct = t.time_added
			loct = utct.replace(tzinfo=utc).astimezone(tz)
			dates_from.append(loct)
			utct = t.time_valid
			loct = utct.replace(tzinfo=utc).astimezone(tz)
			dates_to.append(loct)
		values = {'tasks': tasks, 'dates_from': dates_from, 'dates_to': dates_to}
		values.update(logged())
		self.response.out.write(template.render('tasks_view.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
