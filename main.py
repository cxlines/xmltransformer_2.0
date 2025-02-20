import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
import subprocess
import calendar

def get_last_day_of_month(date_str):
    """Calculate the last day of the given month (format YYYY-MM-DD)"""
    try:
        year, month, _ = map(int, date_str.split('-'))
        last_day = calendar.monthrange(year, month)[1]
        return f"{year}-{month:02d}-{last_day:02d}"
    except ValueError:
        return None  # Invalid date format

def browse_file():
    """Open file dialog to select a file"""
    filepath = filedialog.askopenfilename()
    entry_filepath.delete(0, tk.END)
    entry_filepath.insert(0, filepath)

def save_and_run():
    """Get input values, compute last day of the month, and run scripts"""
    date = entry_date.get()
    company = entry_company.get()
    prefix = entry_prefix.get()
    filepath = entry_filepath.get()

    if not date or not company or not prefix or not filepath:
        messagebox.showerror("Error", "All fields are required!")
        return

    datelastday = get_last_day_of_month(date)

    if not datelastday:
        messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD")
        return

    try:
        # Run idtransformer.py first
        subprocess.run(["python", "idtransformer.py", filepath, prefix, date, company, datelastday], check=True)
        # Run zavtransformer.py second
        subprocess.run(["python", "zavtransformer.py", filepath, prefix, date, company, datelastday], check=True)

        messagebox.showinfo("Success", f"Scripts executed successfully!\nLast day of the month: {datelastday}")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Execution Error", f"An error occurred while running scripts:\n{e}")

# Create the main window
root = ttk.Window(themename="darkly")  # Modern dark mode UI
root.title("TMRP - XML Transformer")
root.geometry("700x350")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=8)
style.configure("TEntry", font=("Arial", 12), padding=5)

# Title
title_label = ttk.Label(root, text="Zadajte informácie", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Frame for input fields
frame = ttk.Frame(root)
frame.pack(pady=5, padx=20, fill="x")

# Labels and Entry Fields
ttk.Label(frame, text="Dátum (RRRR-MM-DD):", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry_date = ttk.Entry(frame, width=30)
entry_date.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Firma:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
entry_company = ttk.Entry(frame, width=30)
entry_company.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Prefix:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
entry_prefix = ttk.Entry(frame, width=30)
entry_prefix.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame, text="Vstupný subor:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
entry_filepath = ttk.Entry(frame, width=30)
entry_filepath.grid(row=3, column=1, padx=10, pady=5)

browse_button = ttk.Button(frame, text="Hľadať", command=browse_file, bootstyle="primary")
browse_button.grid(row=3, column=2, padx=10, pady=5)

# Go Button
go_button = ttk.Button(root, text="Go!", command=save_and_run, bootstyle="success")
go_button.pack(pady=20)

# Run the application
root.mainloop()
