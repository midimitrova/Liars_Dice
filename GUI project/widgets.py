from tkinter import *

class CreateWidgets:
    # Create window and frames
    def create(self):
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title("Liar's Dice")
        self.window.iconbitmap('dice.ico')

        self.top_frame = Frame(self.window)
        self.top_frame.pack(side=TOP)

        self.middle_frame = Frame(self.window)
        self.middle_frame.pack(side=TOP)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack(side=TOP)

        self.result_label = Label(self.bottom_frame, text="", font=("Arial", 16))
        self.result_label.pack(side=LEFT)

        self.entry_label = Entry(self.window)
        self.entry_label.pack(side=TOP)

        self.name_label = Label(self.bottom_frame, text="", font=("Arial", 16))
        self.name_label.pack(side=LEFT)