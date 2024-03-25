
from tkinter import messagebox
import tkinter.messagebox

def showtime(event):
    button = event.widget
    button.config(bg='LightGray')

def showtimeends(event):
    button = event.widget
    button.config(bg='White')

def btime(event):
    button = event.widget
    button.config(bg='snow2',fg='DodgerBlue4')

def btimeends(event):
    button = event.widget
    button.config(bg='DodgerBlue4',fg='snow2')

def btime1(event):
    button = event.widget
    button.config(bg='old lace',fg='DarkOrchid4')

def btimeends1(event):
    button = event.widget
    button.config(bg='DarkOrchid4',fg='old lace')

def adtime(event):
    button = event.widget
    button.config(fg='olive drab',bg='lemon chiffon')

def adtimeends(event):
    button = event.widget
    button.config(bg='olive drab',fg='lemon chiffon')

def E_lg_login_btn(event):
    button = event.widget
    button.config(bg='forest green',fg='White')
    
def L_lg_login_btn(event):
    button = event.widget
    button.config(bg='dodger blue',fg='White')

def opt_btn(event):
    button=event.widget
    button.config(bg='light pink',fg='misty rose')

def opt_ebtn(event):
    button=event.widget
    button.config(bg='misty rose',fg='light pink')

def opt_btn1(event):
    button=event.widget
    button.config(bg='Sky Blue3',fg='gold')

def opt_ebtn1(event):
    button=event.widget
    button.config(bg='sandy brown',fg='gold')

def opt_btn2(event):
    button=event.widget
    button.config(bg='sandy brown',fg='gold')

def opt_ebtn2(event):
    button=event.widget
    button.config(bg='Sky Blue3',fg='gold')

def E_reciept(event):
    button = event.widget
    button.config(bg='LightGray', state='disable')


def L_reciept(event):
    button = event.widget
    button.config(bg='White', state='normal')


    
