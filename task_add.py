#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from logged import *
from datetime import timedelta, datetime
from sets import Set
from db_scheme import *
from pytz_mini import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		categories = db.GqlQuery("SELECT * FROM Category ORDER BY name")
		days = list()
		utc = timezone('UTC')
		tz = timezone('Warsaw')
		for x in range(1,15):
			utct = datetime.now() + timedelta(days=x)
			loct = utct.replace(tzinfo=utc).astimezone(tz)
			days.append(loct)
		values = {'categories': categories, 'days': days, 'valid_days': 7}
		values.update(logged())
		self.response.out.write(template.render('task_add.html', values))
	
	def post(self):
		errors = Set()
		if not self.request.get('title'):
			errors.add('e_no_title')
		if not self.request.get('description'):
			errors.add('e_no_description')
		if not self.request.get('price'):
			errors.add('e_no_price')
		else:
			price = self.request.get_range('price', 0, 9999, 0)
			if price == 0:
				errors.add('e_price')

		if len(errors) == 0:
			task = Task(state = 0, category = db.Key().from_path('Category', int(self.request.get('category'))), title = self.request.get('title'),
				description = self.request.get('description'), private_info = self.request.get('private_info'), price = price,
				time_valid = datetime.now() + timedelta(days=int(self.request.get('valid_days'))), ip_added = self.request.remote_addr)
			task.put()
			session = Session()
			session['task_id'] = task.key().id()
			self.redirect('task_confirm.html') 
			return

		categories = db.GqlQuery("SELECT * FROM Category ORDER BY name")
		days = list()
		utc = timezone('UTC')
		tz = timezone('Warsaw')
		for x in range(1,15):
			utct = datetime.now() + timedelta(days=x)
			loct = utct.replace(tzinfo=utc).astimezone(tz)
			days.append(loct)
		values = {'categories': categories, 'days': days, 'category': int(self.request.get('category')), 'valid_days': int(self.request.get('valid_days')),
			'title': self.request.get('title'), 'description': self.request.get('description'), 'private_info': self.request.get('private_info'),
			'price': self.request.get('price'), 'errors': errors}
		values.update(logged())
		self.response.out.write(template.render('task_add.html', values))
	
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()

