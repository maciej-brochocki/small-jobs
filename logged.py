from db_scheme import *
from sessions import *

def logged():
	session = Session()
	try:
		student = db.get(db.Key.from_path('Student', session['student_id']))
		if student:
			return {'logged': student.nick}
		else:
			session.delete()
			return {}
	except:
		try:
			client = db.get(db.Key.from_path('Client', session['client_id']))
			if client:
				return {'logged': client.email}
			else:
				session.delete()
				return {}
		except:
			return {}

def log_student():
	session = Session()
	try:
		student = db.get(db.Key.from_path('Student', session['student_id']))
		if student:
			return student
		else:
			session.delete()
			return
	except:
		return

def log_client():
	session = Session()
	try:
		client = db.get(db.Key.from_path('Client', session['client_id']))
		if client:
			return client
		else:
			session.delete()
			return
	except:
		return
