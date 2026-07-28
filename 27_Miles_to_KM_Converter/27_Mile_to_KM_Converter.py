from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile-to-KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

#Labels
miles_label = Label(text="miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="km", font=("Arial",12, "bold"))
km_label.grid(column=2, row=1)

is_equal_to_label= Label(text="is equal to", font=("Arial",12, "bold"))
is_equal_to_label.grid(column=0, row=1)

#Insert calculated result in km
kilometer_result_label = Label(text="result", font=("Arial", 12))
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(text="0")

#Entry
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
