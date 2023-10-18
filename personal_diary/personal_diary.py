import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import datetime

def save_entry():
    entry = text.get("1.0", "end-1c")
    if entry:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        category = category_var.get()
        with open("diary.txt", "a") as file:
            file.write(f"Timestamp: {timestamp}\n")
            if category:
                file.write(f"Category: {category}\n")
            file.write(entry + "\n")
        messagebox.showinfo("Success", "Diary entry saved!")
        text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Your diary entry is empty.")

def view_entries():
    with open("diary.txt", "r") as file:
        diary_contents = file.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, diary_contents)

def search_entries():
    search_text = simpledialog.askstring("Search", "Enter search term:")
    with open("diary.txt", "r") as file:
        diary_contents = file.read()
        entries = diary_contents.split("Timestamp: ")
        found_entries = [entry for entry in entries if search_text in entry]
        if found_entries:
            search_result = "Timestamp: " + "\nTimestamp: ".join(found_entries)
            text.delete("1.0", tk.END)
            text.insert(tk.END, search_result)
        else:
            messagebox.showinfo("Search Result", "No matching entries found.")

app = tk.Tk()
app.title("Personal Diary")

style = ttk.Style()
style.configure("TButton", padding=(5, 5, 5, 5))

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

text = tk.Text(frame, height=10, width=40)
text.grid(column=0, row=0, columnspan=3)

category_var = tk.StringVar()
category_entry = ttk.Entry(frame, textvariable=category_var)
category_label = ttk.Label(frame, text="Category:")
category_label.grid(column=0, row=1, sticky=tk.W)
category_entry.grid(column=1, row=1, columnspan=2, sticky=(tk.W, tk.E))

save_button = ttk.Button(frame, text="Save Entry", command=save_entry)
view_button = ttk.Button(frame, text="View Entries", command=view_entries)
search_button = ttk.Button(frame, text="Search Entries", command=search_entries)

save_button.grid(column=0, row=2, pady=5)
view_button.grid(column=1, row=2, pady=5)
search_button.grid(column=2, row=2, pady=5)

app.mainloop()
