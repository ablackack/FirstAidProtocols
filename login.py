import json
import hashlib


class Users():
	def _init_(self):
		return True

	def hash(self, val):
		return hashlib.sha512(val.encode('utf-8')).hexdigest()

	def create(self, name, passwd):
		with open("__users.json") as jdata:
			data = json.load(jdata)
			jdata.close()

		jdata['Users'][name] = str(hash(passwd))

	def login(self, name, passwd):
		passwdhash = hash(passwd)
