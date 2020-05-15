#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################
Name:       Pomodoro
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86
##########################################################
"""

"""
Links:

https://realpython.com/playing-and-recording-sound-python/

https://simpleaudio.readthedocs.io/en/latest/tutorial.html
"""

from tkinter import *
from tkinter.messagebox import *
import simpleaudio as sa

class Pomodoro():
    def __init__(self, master, *args, **kwarg):
        self.app = master
        self.app.geometry("300x105")
        self.app.title("Pomodoro")
        self.app.resizable(False,False)
        self.running = False
        self.pomodoro_active = True
        self.time = 5 #1500
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
        self.time_label = Label(self.screen_container, text="25:00", font=('times 25',50),bg="black", fg="orange")
        self.time_label.pack(expand=NO, fill=X)
        self.start_button = Button(self.button_container, bg="black", fg="orange", text="Start", width=13, command=lambda : self.start()).pack(side=LEFT)
        self.stop_button = Button(self.button_container,  bg="black", fg="orange", text="Pause", width=13, command=lambda : self.stop()).pack(side=LEFT)
        self.restart_button = Button(self.button_container,  bg="black", fg="orange", text="Restart", width=13, command=lambda : self.reset()).pack(side=LEFT)
        self.app.bind("<Return>", lambda x: self.start())

    def calculate_time(self):
        self.mins, self.secs = divmod(self.time, 60)
        return "{:02d}:{:02d}".format(self.mins, self.secs)

    def alarm(self):
        soundfile = "alarm.wav"
        wave_obj = sa.WaveObject.from_wave_file(soundfile)
        if self.running == True:
            wave_obj.play()
        else:
            wave_obj.stop()

    def timer(self):
        if self.running is True:
            if self.time <= 0:
                self.alarm()
                showinfo(title="Alert", message="Time...")
                if self.pomodoro_active is True:
                    self.time = 300
                    self.pomodoro_active = False
                else:
                    self.time = 1500
                    self.pomodoro_active = True
            self.time_label.config(text=self.calculate_time())
            self.time -= 1
            self.time_label.after(1000, self.timer)

    def start(self):
        self.app.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        self.app.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        self.app.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 1500
        self.time_label.config(text="25:00")


if __name__ == '__main__':
    root = Tk()
    Pomodoro(root)
    root.mainloop()