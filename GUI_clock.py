import datetime
import time
from datetime import datetime
from datetime import time
from threading import Thread
from time import sleep
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as ui
from PIL import ImageTk, Image
from pygame import mixer

bga = '#00796B'
window = ui.Tk()
window.title("Alarm")
window.geometry('400x280')
window.config(bg='#BDBDBD')
frame_line = Frame(window, width=400, height=5, bg='#E0E0E0')
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=350, bg=bga)
frame_body.grid(row=1, column=0)


def Activate():
    t = Thread(target=alarm)
    t.start()
def Deactivete():
    print("deactivated",selected.get())
    mixer.music.stop()
    update_clock()

selected = IntVar()
# IMAGE
img = Image.open('alarm-clock.png')
img = ImageTk.PhotoImage(img)
img_app = Label(frame_body, height=100, image=img, bg=bga)
img_app.place(x=30, y=20)

# HOUR
hour = Label(frame_body, text='hours', height=1, font=('Ivy 11 bold'), bg=bga)
hour.place(x=110, y=25)
c_hour = Combobox(frame_body, width=5, font=('arial 10'))
c_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08',
                    '09', '10', '11', '12', '13', '14', '15', '16', '17',
                    '18', '19', '20', '21', '22', '23', '24')
c_hour.current(0)
c_hour.place(x=110, y=50)

# MINUTE
minute = Label(frame_body, text='minutes', height=1, font=('Ivy 11 bold'), bg=bga)
minute.place(x=180, y=25)
c_minute = Combobox(frame_body, width=5, font=('arial 10'))
c_minute['values'] = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '31',
                      '32', '33', '34', '35', '36', '37', '38', '39',
                      '40', '41', '42', '43', '44', '45', '46', '47',
                      '48', '49', '50', '51', '52', '53', '54', '55',
                      '56', '57', '58', '59', '60')
c_minute.current(0)
c_minute.place(x=180, y=50)

# SECOND
second = Label(frame_body, text='seconds', height=1, font=('Ivy 11 bold'), bg=bga)
second.place(x=250, y=25)
c_second = Combobox(frame_body, width=5, font=('arial 10'))
c_second['values'] = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '31',
                      '32', '33', '34', '35', '36', '37', '38', '39',
                      '40', '41', '42', '43', '44', '45', '46', '47',
                      '48', '49', '50', '51', '52', '53', '54', '55',
                      '56', '57', '58', '59')
c_second.current(0)
c_second.place(x=250, y=50)

# period
period = Label(frame_body, text='period', height=1, font=('Ivy 11 bold'), bg=bga)
period.place(x=320, y=25)
c_period = Combobox(frame_body, width=5, font=('arial 10'))
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=320, y=50)


def update_clock():
    now = datetime.now()
    hours_ =now.strftime('%I')
    minutes_ = now.strftime('%M')
    seconds_ = now.strftime('%S')
    am_or_pm = c_period.get()
    time_text = hours_ + ":" + minutes_ + ":" + seconds_ + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)
def update_clock_():
    now = datetime.now()
    hours_ =now.strftime('%I')
    minutes_ = now.strftime('%M')
    seconds_ = now.strftime('%S')
    am_or_pm = c_period.get()
    time_text = hours_ + ":" + minutes_ + ":" + seconds_ + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)


digital_clock_lbl = ui.Label(frame_body, text="00:00:00", font="Helvetica 25 bold", bg=bga)
digital_clock_lbl.place(x=125, y=115)
update_clock()

button = Button(frame_body, text="Set Alarm", font=("Helvetica 15"), command=Activate, bg='#00897B')
button.place(x=89, y=200)

button2 = Button(frame_body, text="Deactevate", font=("Helvetica 15"), command=Deactivete, bg='#00897B')
button2.place(x=220, y=200)


def alarm_sound():
    mixer.music.load('alarm_anime.mp3')
    mixer.music.play()
    selected.set(0)


def alarm():
    while True:
        alarmHour = c_hour.get()
        alarmMinute = c_minute.get()
        alarmSecond = c_second.get()
        alarmPeriod = c_period.get()
        alarmPeriod = str(alarmPeriod).upper()

        now = datetime.now()

        Hour = now.strftime("%I")
        Minute = now.strftime("%M")
        Sconde = now.strftime("%S")
     #   Period = now.strftime("%P")
   # if alarmPeriod == Period:
        if alarmHour == Hour:
            if alarmMinute == Minute:
                if alarmSecond == Sconde:
                    print('Wake Wake Wake Up!')
                    alarm_sound()
    sleep(1)


mixer.init()
# alarm_sound()
window.mainloop()
