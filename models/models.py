from flask import Flask, request, json
from mongokit import *
from config.config import MONGOHQ_URL, DATABASE_NAME
import datetime, re

connection = Connection(MONGOHQ_URL)

class RestDocument(Document):

	def commit_model(self):
		try:
			self.validate()
			self.save()
		except Exception, e:
			return json.dumps({"status" : "fail", "reason" : str(e)})
			
		return self.to_json()

	def update_from_dict(self, dic, exclude=[], email=None):

		if not email is None:
			self['email'] = unicode(email)

		for key_name, key_type in self.structure.items():
			if key_name in dic.keys() and not key_name in exclude:
				try:
					self[key_name] = key_type(dic[key_name])
				except ValueError, e:
					pass


	def json_array(self):
		arr = [ i.to_json_type() for i in self.find() ]
		print "Returning ", len(arr), "elements."
		return json.dumps(arr)

	def as_json_array_by_email(self, email):
		arr = [ i.to_json_type() for i in self.find({'email' : email}) ]
		print "Returning ", len(arr), "elements."
		return json.dumps(arr)

	def json_one(self, _id):
		obj = self.one({'_id' : ObjectId(_id)})
		if obj == None:
			return json.dumps({"status" : "fail", "reason" : "Object does not exist."})
		else:
			print "Returning one element."
			return obj.to_json()

	def json_one_by_email(self, email):
		obj = self.one({'email' : email})
		if obj == None:
			return json.dumps({"status" : "fail", "reason" : "Object does not exist."})
		else:
			print "Returning one element."
			return obj.to_json()

	def as_json(self, _id, email):

		if _id == None:
			return self.as_json_array_by_email(email)
		else:
			return self.json_one(_id)

	def as_json_by_email(self, email=None):

		if email == None:
			return self.json_array()
		else:
			return self.json_one_by_email(email)

	def delete(self, _id=None):

		print "Received DELETE"
		if _id == None:
			return json.dumps({"status" : "fail", "reason" : "no id given"})
		else:
			try:
				self.remove({'_id' : ObjectId(_id)})
				return OK
			except Exception, e:
				return json.dumps({"status" : "fail", "reason" : str(e)})

# 1
@connection.register
class SomeItem(RestDocument):

	use_dot_notation = True
	__collection__ = 'someitems'
	__database__ = DATABASE_NAME
	structure = {
		'email' : unicode,
		'name' : unicode,
		'value_1' : unicode,
		'value_2' : unicode,
		'value_3' : unicode,
		'date_creation' : datetime.datetime
	}

	required_fields = ['email', 'name', 'value_1', 'value_2', 'value_3']
	default_values = {'date_creation' : datetime.datetime.utcnow}

