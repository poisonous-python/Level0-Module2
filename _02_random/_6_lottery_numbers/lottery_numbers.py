import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    no1=random.randint(0,9)
    no2=random.randint(0,9)
    no3=random.randint(0,9)
    no4=random.randint(0,9)
    no5=random.randint(0,9)
    no6=random.randint(0,9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    ticket= str (no1)+str(no2)+str(no3)+str(no4)+str(no5)+str(no6)
    messagebox.showinfo(message="your ticket is:\n"+ ticket)
    print(ticket)
    no7=random.randint(0,9)
    no8=random.randint(0,9)
    no9=random.randint(0,9)
    no10=random.randint(0,9)
    no11=random.randint(0,9)
    no12=random.randint(0,9)
    winner=str(no7)+str(no8)+str(no9)+str(no10)+str(no11)+str(no12)
    messagebox.showinfo(message="The winner is...")
    messagebox.showinfo(message="The winner is...\n"+ winner+"!!!!")
    print("winner: "+ winner)

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
