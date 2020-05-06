from tkinter import *
import tkinter.messagebox


class Pomodoro():

    def __init__(self, master, **kwargs):
        self.app = master
        self.app.geometry("300x185")
        self.app.title("Pomodoro")
        self.app.resizable(False,False)
        self.running = False
        self.pomodoro = True
        self.time = 1500
        self.mins = 0
        self.secs = 0
        self.interface()

    def interface(self):
        self.main_container = Frame(self.app, bg="gray")
        self.main_container.pack(expand=YES, fill=BOTH)

        self.screen_container = Frame(self.main_container, bg="orange", height=75, width=100)
        self.screen_container.pack(expand=NO, fill=X)

        self.button_container = Frame(self.main_container, bg="white", height=25, width=100)
        self.button_container.pack(expand=NO, fill=X)

        self.time_label = Label(self.screen_container, text="25:00", font=('times 25',50),bg="black", fg="orange", height=2)
        self.time_label.pack(expand=NO, fill=X)

        self.start_button = Button(self.button_container, text="Start", width=13, command=lambda : self.start()).pack(side=LEFT)
        self.pause_button = Button(self.button_container, text="Pause", width=13, command=None).pack(side=LEFT)
        self.restart_button = Button(self.button_container, text="Restart", width=13, command=None).pack(side=LEFT)


    def calculate_time(self):
        self.mins, self.secs = divmod(self.time, 60)
        return "{:02d}:{:02d}".format(self.mins, self.secs)


    def timer(self):
        if self.running is True:
            if self.time <= 0:
                if self.pomodoro is True:
                    self.time = 300
                    self.pomodoro = False
                else:
                    self.time = 1500
                    self.pomodoro = True
            self.time_label.config(text=self.calculate_time())
            self.time -= 1
            self.after(1000, self.timer)

    def start(self):
        #self.start_button.config(text="counting...")
        self.running = True
        self.timer()



if __name__ == '__main__':
    root = Tk()
    Pomodoro(root)
    root.mainloop()