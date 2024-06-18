from calendar import DateEntry
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("finance. db")
cur = connection.cursor()
cur.execute(
    """
    CREAT TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        type TEXT,
        amount REAL,
        comment TEXT
)
    
"""
)

connection.commit()

root = Tk()
root.title("Домашня бухгалтерія")
root.geometry("700x340")
root.resizable(width: False, height: False)

left_frame = Frame(root, bd=2, relief=SUNKEN)
left_frame.pack(side=LEFT, pady=10)

date_label = Label(left_frame, text="Дата:")
date_label.pack(anchor="w", pady=10, padx=10)
date_entry = DateEntry(left_frame, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd.mm.y")
date_entry.pack(anchor="w", padx=10)


root.mainloop()

connection.close()