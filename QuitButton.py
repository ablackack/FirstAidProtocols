from tkinter import *


class QuitButton(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		self['text'] = 'Quit'
		# Command to close the window (the destroy method)
		self['command'] = parent.destroy


class MainQuitButton(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		self['text'] = 'Quit'
		# Command to close the window (the destroy method)
		self['command'] = parent.quit
