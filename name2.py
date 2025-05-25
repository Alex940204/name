#!/usr/bin/env python3
from tkinter import*
window = Tk()
window.title('number')
window.minsize(width=500, height=500)
window.resizable(width=False, height=False)

label = Label(text="\nU12127017 林哲宇", font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")

label.pack()

window.mainloop()
