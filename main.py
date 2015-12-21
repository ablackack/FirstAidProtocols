from tkinter import *
from QuitButton import MainQuitButton
from NewPat import NewPat
from ManageSan import ManageSan
from Users import Users

root = Tk()
root.grid()
root.title = "Schulsanitätsdienst"
root.wm_title("Schulsanitätsdienst")

# Variable declaration

usr = Users()

# Add buttons to main window

# button for adding a new patient
btnew_pat = Button(root, text="Neuer Patient", command=NewPat)
btnew_pat.grid(sticky=W+E, pady=1, padx=1)

# button for managing first responsers
btnew_san = Button(root, text="Sanitäter verwalten", command=ManageSan)
btnew_san.grid(sticky=W+E, pady=1, padx=1)

# button for quitiing program
btroot_quit = MainQuitButton(root)
btroot_quit['text'] = "Beenden"
btroot_quit.grid(sticky=W+E, pady=1, padx=1)

usr._init_()
if usr.check("admin", "test"):
	print("Logged in")
else:
	print("Wrong user or password")

root.mainloop()
