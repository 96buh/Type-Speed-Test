from tkinter import *


class ChooseWord:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Proficiency Test")
        self.window.config(padx=50, pady=50)
        self.WORD_NUMBER = 10

        self.title = Label(text="Select", font=("Arial", 30))
        self.title.grid(row=0, column=0, columnspan=4, pady=30)

        self.button_10 = Button(text="10", font=("Arial", 20), width=8, command=self.set_10)
        self.button_10.grid(row=1, column=0, padx=40)

        self.button_25 = Button(text="25", font=("Arial", 20), width=8, command=self.set_25)
        self.button_25.grid(row=1, column=1, padx=40)

        self.button_50 = Button(text="50", font=("Arial", 20), width=8, command=self.set_50)
        self.button_50.grid(row=1, column=2, padx=40)

        self.button_100 = Button(text="100", font=("Arial", 20), width=8, command=self.set_100)
        self.button_100.grid(row=1, column=3, padx=40)

        self.window.mainloop()

    def set_10(self):
        self.WORD_NUMBER = 10
        self.window.destroy()
    def set_25(self):
        self.WORD_NUMBER = 25
        self.window.destroy()
    def set_50(self):
        self.WORD_NUMBER = 50
        self.window.destroy()
    def set_100(self):
        self.WORD_NUMBER = 100
        self.window.destroy()


