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
		session = Session()
		try:
			task = db.get(db.Key.from_path('Task', session['task_id']))
			session.delete_item('task_id')
			client = db.get(db.Key.from_path('Client', session['client_tmp']))
			session.delete_item('client_tmp')
			task.client = client
			task.put()
			values = {'task': 1}
			values.update(logged())
		except:
			values = logged()
		self.response.out.write(template.render('client_confirm.html', values))
		
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
