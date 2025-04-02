
# import random module
import random
# import tkinter
from tkinter import *

# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
# Title of the container
root.title('Love Calculator 💕')

# Function to calculate love percentage
def calculate_love():
    # Check if both input fields have values
    if name1.get().strip() == "" or name2.get().strip() == "":
        result.config(text="Please enter the value!", fg="red")
    else:
        # Generate a random double-digit value
        love_percentage = random.randint(10, 99)
        result.config(text=f"Love Percentage: {love_percentage}%", fg="green")

# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", pady=3)
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:", pady=3)
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

# Button to calculate love percentage
bt = Button(root, text="Calculate", height=1, pady=3, width=7, command=calculate_love)
bt.pack()

# Text on result slot
result = Label(root, text='Love Percentage between both of You:')
result.pack()

# Starting the GUI
root.mainloop()
