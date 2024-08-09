import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo(message="Welcome to 8 ball!\n"+ "Get ready to see your fortune!")
    # TODO Get the user to enter a question for the 8 ball to answer
    for i in range(5):
        userquestion= simpledialog.askstring(title="Ask your question", prompt="What question do you have for the 8 ball?")
    # Make a variable and initialize it to a random number between 0 and 3
        answer= random.randint(0, 3)
    # If the random number is 0
        if answer==0:
            messagebox.showinfo(message="Yes!")
        # tell the user "Yes"

    # If the random number is 1
        elif answer==1:
            messagebox.showinfo(message="No")
        # tell the user "No"

    # If the random number is 2
        elif answer==2:
            messagebox.showinfo(message="Uhh\n Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
        elif answer==3:
            messagebox.showinfo(message="It all depends on what happens at the apocalypse")
    messagebox.showinfo(message="I'm afraid that's all the time we have!")
        # write your own answer
window.mainloop()
