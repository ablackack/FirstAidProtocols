from tkinter import *

def changeTitle():
	test.wm_title("This Is A Test!")

test = Tk()
test.geometry()


label = Label(test, text="Dies ist ein Test. Hallo, Welt!")
label.place(x=6, y=6, height=10)

button = Button(test, text="Test this!", command=changeTitle)
button.place(x=6, y=20, height=40, width=100)

test.mainloop()