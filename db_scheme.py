#!/usr/bin/env python

from google.appengine.ext import db

class Category(db.Model):
	name = db.StringProperty(required=True)

class Voivodeship(db.Model):
	name = db.StringProperty(required=True)

class City(db.Model):
	voivodeship = db.ReferenceProperty(Voivodeship)
	name = db.StringProperty(required=True)
	people = db.IntegerProperty(required=True)

class District(db.Model):
	city = db.ReferenceProperty(City)
	name = db.StringProperty(required=True)
	
class Student(db.Model):
	type = db.IntegerProperty(required=True) # 0-student, 1-firma
	nick = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	phone = db.PhoneNumberProperty(required=True)
	city = db.ReferenceProperty(City)
	district = db.ReferenceProperty(District)
	email = db.EmailProperty(required=True)
	password = db.StringProperty(required=True)
	spam = db.BooleanProperty(required=True)
	active = db.BooleanProperty(required=True)
	avatar = db.BlobProperty()
	specialities = db.ListProperty(db.Key)
	description = db.StringProperty()
	notify = db.IntegerProperty(required=True) # 0-kazda nowa, 1-raz dziennie, 2-nie chce

class Client(db.Model):
	type = db.IntegerProperty(required=True) # 0-osoba prywatna, 1-firma
	name = db.StringProperty(required=True)
	phone = db.PhoneNumberProperty(required=True)
	city = db.ReferenceProperty(City)
#	district = db.ReferenceProperty(District)
	district = db.StringProperty()
	email = db.EmailProperty(required=True)
	password = db.StringProperty(required=True)
	spam = db.BooleanProperty(required=True)
	active = db.BooleanProperty(required=True)
	notify = db.IntegerProperty(required=True) # 0-kazda nowa, 1-raz dziennie, 2-nie chce

class Task(db.Model):
	client = db.ReferenceProperty(Client)
	state = db.IntegerProperty(required=True) # 0-not active, 1-active
	category = db.ReferenceProperty(Category)
	title = db.StringProperty(required=True)
	description = db.StringProperty(required=True)
	private_info = db.StringProperty()
	price = db.IntegerProperty(required=True)
	time_added = db.DateTimeProperty(auto_now_add=True)
	time_valid = db.DateTimeProperty(required=True)
	ip_added = db.StringProperty(required=True)
	selected_offer = db.Key

class Offer(db.Model):
	student = db.ReferenceProperty(Student)
	task = db.ReferenceProperty(Task)
	price = db.IntegerProperty(required=True)
	info = db.StringProperty()
	time_added = db.DateTimeProperty(auto_now_add=True)
	ip_added = db.StringProperty(required=True)

class Comment(db.Model):
	student = db.ReferenceProperty(Student)
	task = db.ReferenceProperty(Task)
	rating = db.IntegerProperty(required=True)
	info = db.StringProperty(required=True)
