import random
from tkinter import *
import string


# defining the generator
def generator():

    Capital_letter = string.ascii_uppercase
    small_letter = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    all = Capital_letter + small_letter + numbers + symbols
    password = int(length_box.get())

    if choice.get() ==1:
        PasswordField.insert(0, random.sample(small_letter, password))
    if choice.get() ==2:
        PasswordField.insert(0, random.sample(all, password))

# using python GUI - tkinter,(root),background-Black,
# font= ariel (BOLD)

root = Tk()
root.config(bg='black')

choice = IntVar()
Font = "ariel", 13, "bold"

# heading of password generator GUI
# text, font, size of font,background

passwordGeneratorLabel = Label(root, text='GROUP 8 PASSWORD GENERATOR', bg='dark blue', font=("new roman", 30, 'bold', ), fg= 'white')
passwordGeneratorLabel.grid()

# creating a button: weak and heavy button

weakradioButton = Radiobutton(root, text="WEAK PASSWORD", value=1, variable=choice, font=Font, )
weakradioButton.grid(pady=8)
heavyradioButton = Radiobutton(root, text="STRONG PASSWORD", value=2, variable=choice, font=Font)
heavyradioButton.grid(pady=8)

lengthlLabel = Label(root, text="PASSWORD", font=Font)
lengthlLabel.grid(pady=8)

length_box = Spinbox(root, from_=1, to_=10, width=5, font=Font)
length_box.grid()

GenerateButton = Button(root, text='GENERATE', font=Font, command=generator)
GenerateButton.grid(pady=10)

PasswordField = Entry(root, width=50, bd=10)
PasswordField.grid(pady=10)

root.mainloop()
