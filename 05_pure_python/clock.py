import tkinter as tk
from time import strftime

# create window
root = tk.Tk()
root.title("Digital Clock")

# function to update time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# clock label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()