import json
import hashlib
from tkinter import *
from QuitButton import QuitButton


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

	def show_login_window(self):
		def login():
			name = usrname.get()
			passwd = usrpasswd.get()

			if self.check(name, passwd) and (login_attempts < max_login_attempts):
				print("User " + name + " logged in successfully")
				lroot.destroy()
			else:
				print("User " + name + " cannot be logged in: Wrong username/password")

		# declaring variables
		max_login_attempts = 3  # specifies the max amount of login attempts the user can take before getting blocked
		login_attempts = 1

		lroot = Tk()
		lroot.grid()
		lroot.title = "Login"
		lroot.wm_title("Login")

		# Adding elements to window

		# input fields

		# username
		lbusrname = Label(lroot, text="Username:")
		lbusrname.grid(pady=1, padx=1, row=0, column=0)

		usrname = Entry(lroot)
		usrname.grid(pady=1, padx=1, row=0, column=1)

		# password
		lbusrpasswd = Label(lroot, text="Passwort:")
		lbusrpasswd.grid(pady=1, padx=1, row=1, column=0)

		usrpasswd = Entry(lroot, show="*")
		usrpasswd.grid(pady=1, padx=1, row=1, column=1)

		# buttons

		# login
		btlogin = Button(lroot, text="Login", command=login)
		btlogin.grid(pady=1, padx=1, row=2, column=1, sticky="E")

		# closing the window
		btquit = QuitButton(lroot)
		btquit['text'] = "Schließen"
		btquit.grid(pady=1, padx=1, row=2, column=1, sticky="W")

		lroot.mainloop()
