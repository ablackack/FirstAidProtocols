from tkinter import *
from QuitButton import QuitButton
from Users import Users

class LoginWindow:
	def __init__(self):
		# Variable declarations

		max_login_attempts = 3  # specifies the max amount of login attempts the user can take before getting blocked
		login_attempts = 1
		usr = Users()
		usr._init_()

	def login(self):
		name = self.usrname.get()
		passwd = self.usrpasswd.get()

		if self.usr.check(name, passwd) and (self.login_attempts < self.max_login_attempts):
			print("User " + name + " logged in successfully")
			self.lroot.destroy()
		else:
			print("User " + name + " cannot be logged in: Wrong username/password")

	def create_window(self):
		# starting main loop
		self.lroot.mainloop()

	# declaring window variables
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
