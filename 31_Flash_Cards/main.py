#----------------- LINKS TO TRANSLATION TOOLS ----------------------------#
#https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
#https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
#https://support.google.com/docs/answer/3093331?hl=en-GB
#https://docs.cloud.google.com/translate/docs/languages?hl=en
#https://www.opensubtitles.org/en/search/subs
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

#----------------- FLIP CARD ---------------------------------------------#
#To change the color of the text in a canvas element, use the fill parameter.
## e.g. https://stackoverflow.com/questions/41030973/how-can-i-change-the-color-of-text-in-tkinter
#Tkinter Reference Manual: .after() method: https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm
# Tkinter Reference Manual: .after_cancel() method: https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm


#------------------ SAVE PROGRESS ---------------------------------------#
#https://www.w3schools.com/python/ref_list_remove.asp
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

#------------------------------------------------------------------------#

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}

#----------------- DEFINITION CARD --------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# Learn French word
def next_card():
    global current_card, flip_timer
    window.after_cancel((flip_timer))
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)

# Flip Card English translation word
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

#Save Progress
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

#--------------------- GUI -------------------------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_botton = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_botton.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_botton = Button(image=check_image, highlightthickness=0, command=is_known )
known_botton.grid(row=1, column= 1)


next_card()

window.mainloop()

