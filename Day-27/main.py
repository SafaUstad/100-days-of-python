# Miles to Kilometer Converter Using Tkinter

from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx = 20, pady = 20)

input = Entry()
input.grid(row=0, column=1)
input.config(width=7)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to")
equals_label.grid(row=1, column=0)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def converter():
    miles = float(input.get())
    km = round(miles * 1.60934)
    km_result_label.config(text= km)

button = Button(text="Calculate", command=converter)
button.grid(row=2, column=1)

mainloop()
