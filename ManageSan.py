from tkinter import *
from tkinter import ttk
from QuitButton import QuitButton
import json


class ManageSan:
	def __init__(self):
		# creating the window
		san = Tk()
		san.geometry()
		san.wm_title("Sanitäter verwalten")
		san.configure(width=700, height=800)
		canvas = Canvas(san, width=700, height=800)
		canvas.place(x=0, y=0)
		canvas.create_line(180, 5, 180, 795, fill="grey", tags="line")
		canvas.create_line(5, 155, 180, 155, fill="grey", tags="line")

		def save_new_sani():
			with open("__sanis.json") as jsond:
				jdata = json.load(jsond)
				jsond.close()

			jdata['Sanis'][sanadd_name.get()] = sanadd_class.get()
			with open("__sanis.json", 'w') as f:
				json.dump(jdata, f, sort_keys=True)
				f.close()

			sanis_show()
			print("Sanitäter-Datei aktualisiert.")

		def delete_sani():
			with open("__sanis.json") as jsondata:
				datajson = json.load(jsondata)
				jsondata.close()

#			for jkey in datajson['Sanis'].keys():
#				if jkey == san_del.get():
#					jkey.pop()

			with open("__sanis.json", 'w') as g:
				json.dump(datajson, g, sort_keys=True)
				g.close()

			sanis_show()
			print(san_del.get() + " gelöscht")

		def sanis_show():
			san_show.delete(1.0, END)
			with open("__sanis.json") as jsond:
				jdata = json.load(jsond)
				jsond.close()

			san_show.insert(END, "Name des Sanitäters\t\t\t\t\tKlasse/Stufe\n")
			san_show.insert(END, "----------------------------------------------------\n")
			for key in sorted(jdata['Sanis'].keys()):
				san_show.insert(END, key + "\t\t\t\t\t     "+ jdata['Sanis'][key] + "\n")

		with open("__sanis.json") as json_data:
			data = json.load(json_data)
			json_data.close()

		sanis = []

		for a in data['Sanis']:
			sanis.append(a)

		sanis.sort()
		print(sanis)

		# section for adding a first responder

		lbsanadd_caption = Label(san, text="Sanitäter hinzufügen", font="bald")
		lbsanadd_caption.place(x=2, y=2)

		lbsanadd_name = Label(san, text="Name: ")
		lbsanadd_name.place(x=2, y=25)

		sanadd_name = Entry(san)
		sanadd_name.place(x=2, y=48)

		lbsanadd_class = Label(san, text="Klasse: ")
		lbsanadd_class.place(x=2, y=71)

		sanadd_class = Entry(san)
		sanadd_class.place(x=2, y=94)

		btsanadd_save = Button(san, text="Speichern", command=save_new_sani)
		btsanadd_save.place(x=2, y=117)

		# section for deleting a first responder

		lbsandel_caption = Label(san, text="Sanitäter entfernen", font="bold")
		lbsandel_caption.place(x=2, y=160)

		san_del = ttk.Combobox(san, values=sanis)
		san_del.place(x=2, y=183)

		btsan_del = Button(san, text="Entfernen", command=delete_sani)
		btsan_del.place(x=2, y=206)

		# TODO: Add a combobox for displaying all first responders. Disable edit function!

		# section for editing an existing first responder

		# TODO: Add a form for editing a first responder

		# section for displaying all first responders present in the file

		lbsan_show = Label(san, text="Sanitäter anzeigen", font="bold")
		lbsan_show.place(x=190, y=2)

		san_show = Text(san)
		san_show.place(x=190, y=25, width=500, height=730)
		sanis_show()

		# quitbutton
		btsan_quit = QuitButton(san)
		btsan_quit['text'] = "Schließen"
		btsan_quit.place(x=610, y=767)
