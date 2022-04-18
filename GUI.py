import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.scrolledtext import *


window = Tk()
window.title("Application")
window.geometry("1400x900")
window.config(background='white')

check_me_out = Label(window, text='Check Me Out!', font=("Helvetica", 25, 'bold'), fg='black', bg='white')
check_me_out.place(x=600, y=10)


item_label = Label(window, text='Item', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white')
item_label.place(x=280, y=90)

text_1 = ScrolledText(window,height=35, width=40, border=2)
text_1.place(x=150, y=150)

quantity_label = Label(window, text='Quantity', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white')
quantity_label.place(x=650, y=90)

text_2 = ScrolledText(window,height=35, width=40, border=2)
text_2.place(x=550, y=150)

price_label = Label(window, text='Price', font=("Helvetica", 25, 'bold', 'underline'), fg='black', bg='white')
price_label.place(x=1070, y=90)

text_3 = ScrolledText(window,height=35, width=40, border=2)
text_3.place(x=950, y=150)


remove_item_btn = Button(window, text='Remove Item', width=20, height=2, font=("Helvetica", 14), border=3, cursor='hand2')
remove_item_btn.place(x=170, y=750)

total_label = Label(window, text='Total: ', font=("Helvetica", 25, 'bold'), fg='black', bg='white')
total_label.place(x=1000, y=750)

under_line = Label(window, text='                  ', font=("Helvetica", 25, 'bold','underline'), fg='black', bg='white')
under_line.place(x=1100, y=750)


window.mainloop()