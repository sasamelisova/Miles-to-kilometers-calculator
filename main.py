from tkinter import *
num = 0
window = Tk()
window.title("Miles to km")
window.config(padx=30, pady=30)
num_mile = IntVar()


def button_clicked():
    num_km["text"] = round(float(num_miles.get()) * 1.60934, 2)


miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=1)

miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

num_miles = Entry(width=7, textvariable=num_mile, font=("Arial", 10, "bold"))
num_miles.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 10, "bold"))
km.grid(column=2, row=2)

equal = Label(text="is equal to", font=("Arial", 10, "bold"))
equal.grid(column=0, row=2)

num_km = Label(text="0", font=("Arial", 10, "bold"))
num_km.grid(column=1, row=2)

window.mainloop()

