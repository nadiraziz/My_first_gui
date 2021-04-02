from tkinter import *
KILOMETER = 0
FONT = ('Arial', 14, 'normal')
# Creating a new window and configurations
window = Tk()
window.title("Miles to Km ")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_label.config(text=f"{km}")

# entries
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)


# Labels
label = Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)


# Labels
kilometer_label = Label(text="0", font=FONT)
kilometer_label.grid(column=1, row=1)

# Labels
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)




button_calculate = Button(text="Calculate", font=FONT, command=miles_to_km)
button_calculate.grid(column=1, row=2)



window.mainloop()

