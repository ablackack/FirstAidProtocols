from tkinter import *
from tkinter import ttk
from QuitButton import QuitButton
import time
import json


class NewPat:
	@property
	def __init__(self):
		# creating the window
		pat = Tk()
		pat.geometry()
		pat.wm_title("Neuer Patient")
		pat.configure(width=855, height=500)

		# define variables
		sanis = []
		v_san1 = StringVar(pat)
		v_san2 = StringVar(pat)
		v_san3 = StringVar(pat)
		v_san4 = StringVar(pat)

		# methods

		def get_filename():
			filename = ""
			date = time.strftime("%Y%m%d_%H%M%S")

			filename += date
			filename += "_"

			for c in pat_name.get():
				if c.isalpha():
					filename += c

			filename += ".json"
			return filename

		def save_protocol():
			with open("__template.json") as json_data:
				data = json.load(json_data)
				json_data.close()

			data['Patient']['Name'] = pat_name.get()
			data['Patient']['Klasse'] = pat_class.get()
			data['Patient']['Beginn'] = time_arrive.get()
			data['Patient']['Ende'] = time_leave.get()
			data['Sanis']['Sani1'] = v_san1.get()
			data['Sanis']['Sani2'] = v_san2.get()
			data['Sanis']['Sani3'] = v_san3.get()
			data['Sanis']['Sani4'] = v_san4.get()
			with open(get_filename(), 'w') as f:
				json.dump(data, f, sort_keys=True)
				f.close()

			print("Protokoll unter ", get_filename(), " gespeichert.")

		def receive_message():
			# receive sent message from other instance of program and from unit in schools office
			print("Nachricht von [IP] empfangen")
			chat.insert(END, "[IP]: empfangene Nachricht")

		def send_message():
			print("Nachricht " + message.get() + " gesendet")
			chat.insert(END, "[Ich]: " + message.get() + "\n")
			# clear entry field with title message
			# write message into chat window: done

		def get_sanis():
			sanis.clear()
			with open("sanis.json") as json_data:
				data = json.load(json_data)
				json_data.close()

			for a in data['Sanis']:
				sanis.append(a)

			sanis.sort()

			return sanis

		get_sanis()

		def sanchange(index, value, op):
			get_sanis()
			if v_san1.get() in sanis:
				sanis.remove(v_san1.get())
			if v_san2.get() in sanis:
				sanis.remove(v_san2.get())
			if v_san3.get() in sanis:
				sanis.remove(v_san3.get())
			if v_san4.get() in sanis:
				sanis.remove(v_san4.get())

			san1['values'] = sanis
			san2['values'] = sanis
			san3['values'] = sanis
			san4['values'] = sanis
			print(sanis)

		# window elements

		# inputs

		# name
		lbpat_name = Label(pat, text="Name:")
		lbpat_name.place(x=2, y=2)

		pat_name = Entry(pat)
		pat_name.place(x=44, y=2, width=200)

		# class
		lbpat_class = Label(pat, text="Klasse/Stufe:")
		lbpat_class.place(x=257, y=25)

		pat_class = Entry(pat)
		pat_class.place(x=338, y=25, width=223)

		# stayed time
		lbtime = Label(pat, text="Behandlungszeit (HH:MM):")
		lbtime.place(x=257, y=2)

		time_arrive = Entry(pat)
		time_arrive.place(x=424, y=2, width=50)

		lbbis = Label(pat, text="bis")
		lbbis.place(x=482, y=2)

		time_leave = Entry(pat)
		time_leave.place(x=512, y=2, width=50)

		# info field
		lbinfo = Label(pat, text="Informationen")
		lbinfo.place(x=577, y=2)

		info = Text(pat)
		info.place(x=577, y=25, width=275, height=150)

		# chat window
		lbchat = Label(pat, text="Kommunikation")
		lbchat.place(x=577, y=180)

		chat = Text(pat)
		chat.place(x=577, y=203, width=275, height=210)

		lbmessage = Label(pat, text="Nachricht:")
		lbmessage.place(x=577, y=421)

		message = Entry(pat)
		message.place(x=577, y=444, width=200)

		# first responsers

		lbsan1 = Label(pat, text="Sanitäter 1:")
		lbsan1.place(x=2, y=25)

		# san1 = Entry(pat)
		# san1.place(x=77, y=25)

		san1 = ttk.Combobox(pat, values=sanis, textvar=v_san1)
		san1.place(x=77, y=25)

		lbsan2 = Label(pat, text="Sanitäter 2:")
		lbsan2.place(x=2, y=48)

		# san2 = Entry(pat)
		# san2.place(x=77, y=48)

		san2 = ttk.Combobox(pat, values=sanis, textvar=v_san2)
		san2.place(x=77, y=48)

		lbsan3 = Label(pat, text="Sanitäter 3:")
		lbsan3.place(x=2, y=71)

		# san3 = Entry(pat)
		# san3.place(x=77, y=71)

		san3 = ttk.Combobox(pat, values=sanis, textvar=v_san3)
		san3.place(x=77, y=71)

		lbsan4 = Label(pat, text="Sanitäter 4:")
		lbsan4.place(x=2, y=94)

		# san4 = Entry(pat)
		# san4.place(x=77, y=94)

		san4 = ttk.Combobox(pat, values=sanis, textvar=v_san4)
		san4.place(x=77, y=94)

		# buttons

		# button for saving current protocol
		btpat_save = Button(pat, text="Protokoll speichern", command=save_protocol)
		btpat_save.place(x=709, y=467)

		# button for closing the window
		btpat_quit = QuitButton(pat)
		btpat_quit['text'] = "Schließen"
		btpat_quit.place(x=619, y=467)

		# button for sending chat message
		btsenden = Button(pat, text=">>", command=send_message)
		btsenden.place(x=780, y=444, width=72, height=20)

		# calling callback functions on change

		v_san1.trace('w', sanchange)
		v_san2.trace('w', sanchange)
		v_san3.trace('w', sanchange)
		v_san4.trace('w', sanchange)
