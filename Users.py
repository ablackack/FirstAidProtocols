import json
import hashlib


class Users():
	def _init_(self):
		return True

	def pwhash(self, val):
		return hashlib.sha512(val.encode('utf-8')).hexdigest()

	def load_pwhash(self, name):
		with open("__users.json") as jdata:
			data = json.load(jdata)
			jdata.close()

		return data['Users'][name]

	def create(self, name, passwd):
		with open("__users.json") as jdata:
			data = json.load(jdata)
			jdata.close()

		data['Users'][name] = self.pwhash(passwd)

		with open("__users.json", 'w') as f:
			json.dump(data, f, sort_keys=True)
			f.close()

	def check(self, name, passwd):
		if self.pwhash(passwd) == self.load_pwhash(name):
			return True
		else:
			return False

