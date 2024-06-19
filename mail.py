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

def add_transaction():
        if type_combobox.get() and amount_entry.get():
              try:
                    transaction_type = type_combobox.get()
                    amount = float(amount_entry.get())
                    comment= comment_entry.get()
                    date = date_entry.get()

                    cur.execute("""
                        INSERT INTO transaction (date, type, amount, comment)
                        VALUES(?, ?, ?, ?)""", date, transaction_type, amount, comment)
                    
                transaction_id = cur.lastrowid
              





                except:

root = Tk()
root.title("Домашня бухгалтерія")
root.geometry("700x340")
root.resizable(width:False, height:False)

left_frame = Frame(root, bd=2, relief=SUNKEN)
left_frame.pack(side=LEFT, pady=10)

date_label = Label(left_frame, text="Дата:")
date_label.pack(anchor="w", pady=10, padx=10)
date_entry = DateEntry(left_frame, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd.mm.y")
date_entry.pack(anchor="w", padx=10)

type_label = Label(left_frame, text="Тип:")
type_label.pack(anchor="w", pady=10, padx=10)
type_combobox = ttk.Combobox(left_frame, values=["Прибутки", "Видатки"], state="readonly")
type_combobox.pack(anchor="w", padx=10)

amount_label = Label(left_frame, text="Сума:")
amount_label.pack(anchor="w", pady=10, padx=10)
amount_entry = Entry(left_frame)
amount_entry.pack(anchor="w", padx=10)

comment_label = Label(left_frame, text="Коментарій")
comment_label.pack(anchor="w", pady=10, padx=10)
comment_entry = Entry(left_frame)
comment_entry.pack(anchor="w", padx=10)

add_button = Button(left_frame, text="Додати транзакцію", command=add_transaction)
add_button.pack(anchor="w", pady=10, padx=10)

button_frame = Frame(root, bd=2, relief=SUNKEN)
button_frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

delete_button = Button(button_frame, text="Видалити транзакцію", command=delete_transaction)
delete_button.pack(side=LEFT, padx=10)
delete_all_button = Button(button_frame, text="Видалити всі транзакції", command=delete_all_transactions)
edit_button = Button(button_frame, text="Редагувати транзакцію", command=edit_transaction)
edit_button.pack(side=LEFT, padx=10)

right_frame=Frame(root)
right_frame.pack(side=LEFT, fill=BOTH)

data_frame = Frame(right_frame, bd=2, relief=SUNKEN)
data_frame.pack(sidr=LEFT, fill=BOTH, expand=True)

treeiew=ttk.Treeview(data_frame)
treeiew.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar=ttk.Scrollbar(data_frame, orient="vertical", command=treeiew.yview)
scrollbar.pack(side=RIGHT, fill=Y)
treeiew.configure(yscrollcommand=scrollbar=scrollbar.set)

treeiew["columns"] = ("id", "date", "type", "amount", "comment")
treeiew.column("#0", width=0, stretch=NO)
treeiew.column("id", anchor=W, width=100)
treeiew.column("date", anchor=W, width=100)
treeiew.column("type", anchor=W, width=100)
treeiew.column("amount", anchor=W, width=100)
treeiew.column("comment", anchor=W, width=200)

treeiew.heading("#0", text="")
treeiew.heading("id", text="ID")
treeiew.heading("data", text="Дата")
treeiew.heading("type", text="Тип")
treeiew.heading("amount", text="Сумма, Фунти стерлінги")
treeiew.heading("comment", text="Коментарії")

cur.execute("SELECT * FROM transactions")
rows =cur.fetchall()

for row in rows:
    treeiew.insert(parent:"", END, values=row)




root.mainloop()

connection.close()