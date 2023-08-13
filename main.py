from tkinter import *
import random
import time
from tkinter import messagebox
from choose import ChooseWord

global user_text
global correct_text


class Game:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.wpm = 0
        self.is_timing = False
        self.WORD_NUMBER = ChooseWord().WORD_NUMBER

        # window
        self.window = Tk()
        self.time_label_var = StringVar()
        self.wpm_label_var = StringVar()
        self.window.title("Typing Proficiency Test")
        self.window.config(padx=50, pady=50)
        # window's title
        self.title = Label(text="Typing Test", font=("Arial", 50))
        self.title.grid(row=0, column=1, pady=30)

        # time label
        self.time_label = Label(self.window, text=f"time:{round(self.end_time)}s", font=("Arial", 30),
                                textvariable=self.time_label_var)
        self.time_label.grid(row=0, column=0)

        # wpm label
        self.wpm_label = Label(self.window, text=f"wpm:{round(self.wpm)}s", font=("Arial", 30),
                               textvariable=self.wpm_label_var)
        self.wpm_label.grid(row=0, column=2)

        # text data
        self.text_box = Text(height=5, width=80, font=("Arial", 15))
        self.data = self.create_text()
        self.text_box.insert(END, self.data)
        self.text_box.grid(row=1, column=0, columnspan=3)

        # user input
        self.user_input = Text(height=2, width=80, font=("Arial", 15))
        self.user_input.grid(row=2, column=0, columnspan=3, pady=20)
        self.user_input.focus_set()

        # reset button
        self.reset_button = Button(text="Restart", font=("Arial", 15), command=self.restart)
        self.reset_button.grid(row=3, column=1)

        # functions
        self.check_typing_speed()

        self.window.mainloop()

    def check_typing_speed(self):
        global user_text
        global correct_text
        user_text = self.user_input.get("1.0", "end-1c")
        correct_text = self.text_box.get("1.0", "end-1c")

        self.change_color()
        self.start_timer()
        # 結束後計算WPM
        if user_text == correct_text[:-1]:
            self.end_time = time.time() - self.start_time
            words = len(user_text) / 5
            minute = self.end_time / 60
            wpm = words / minute

            self.wpm_label_var.set(f"wpm: {round(wpm)}")
            messagebox.showinfo("Finish", f"time:{round(self.end_time, 2)}\nwpm:{round(wpm, 2)}")
        else:
            self.update_time_label()
            self.window.after(10, self.check_typing_speed)

    def start_timer(self):
        if not self.is_timing and user_text != "":
            self.start_time = time.time()
            self.is_timing = True

    def restart(self):
        # 刪除測試用單字和使用者輸入
        self.text_box.delete("1.0", END)
        self.user_input.delete("1.0", END)
        # 生成新單字測試
        data = self.create_text()
        self.text_box.insert(END, data)
        self.text_box.grid(row=1, column=0)
        self.is_timing = False
        self.check_typing_speed()
        self.start_time = 0
        self.end_time = 0

    def create_text(self):
        content = ""
        with open("The_Oxford_3000.txt", mode='r', encoding='utf-8') as data:
            words = [word.strip() for word in data.readlines()]
            data = random.sample(words, self.WORD_NUMBER)
        for word in data:
            content += word + " "
        return content

    def change_color(self):
        self.text_box.tag_remove('correct', '1.0', 'end')
        self.text_box.tag_remove('wrong', '1.0', 'end')

        for index, (user_char, correct_char) in enumerate(zip(user_text, correct_text)):
            start_index = f'1.{index}'
            end_index = f'1.{index + 1}'

            if user_char == correct_char:
                self.text_box.tag_add('correct', start_index, end_index)
                self.text_box.tag_config('correct', foreground='green')

            elif user_char != correct_char and user_char != "":
                self.text_box.tag_add('wrong', start_index, end_index)
                self.text_box.tag_config('wrong', foreground='red')

    def update_time_label(self):
        if self.is_timing:
            current_time = time.time() - self.start_time
            self.time_label_var.set(f"time:{round(current_time)}s")
        else:
            self.wpm_label_var.set(f"wpm: 0")
            self.time_label_var.set(f"time: {self.end_time}s")


Game()
