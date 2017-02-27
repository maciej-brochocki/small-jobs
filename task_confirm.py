#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from logged import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		client = log_client()
		if not client:
			session = Session()
			session['after_client_login'] = 'task_confirm.html'
			self.redirect('client_login.html')
			return
		session = Session()
		try:
			task = db.get(db.Key.from_path('Task', session['task_id']))
		except:
			self.redirect('/')
			return
		task.client = client
		task.state = 1
		task.put()
		session.delete_item('task_id')
		self.response.out.write(template.render('task_confirm.html', logged()))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
