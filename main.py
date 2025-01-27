import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Function to handle the "GO!" button click
def start_program():
    csv_file_path = file_path_var.get()
    todaysdate = date_var.get()
    companyname = company_var.get()
    myprefix = prefix_var.get()

    # You can pass these variables to your script or use them as needed
    print(f"CSV File Path: {csv_file_path}")
    print(f"Date: {todaysdate}")
    print(f"Company: {companyname}")
    print(f"Prefix: {myprefix}")

    # Run the idtransformer.py script
    script_path = "idtransformer.py"  # Replace with the actual path if needed
    if os.path.exists(script_path):
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"Script {script_path} not found.")

# Function to open a file dialog
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
    file_path_var.set(file_path)

# Create the main application window
root = tk.Tk()
root.title("XML TRANSFORMER 2o")

# Filepath field
tk.Label(root, text="CSV Súbor:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
file_path_var = tk.StringVar()
tk.Entry(root, textvariable=file_path_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=5)

# Date field
tk.Label(root, text="Datum (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
date_var = tk.StringVar()
tk.Entry(root, textvariable=date_var, width=50).grid(row=1, column=1, padx=10, pady=5)

# Company field
tk.Label(root, text="Firma:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
company_var = tk.StringVar()
tk.Entry(root, textvariable=company_var, width=50).grid(row=2, column=1, padx=10, pady=5)

# Prefix field
tk.Label(root, text="Prefix:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
prefix_var = tk.StringVar()
tk.Entry(root, textvariable=prefix_var, width=50).grid(row=3, column=1, padx=10, pady=5)

# GO button
tk.Button(root, text="GO!", command=start_program, bg="green", fg="white", font=("Arial", 12, "bold")).grid(
    row=4, column=0, columnspan=3, pady=20
)

# Run the application
root.mainloop()
