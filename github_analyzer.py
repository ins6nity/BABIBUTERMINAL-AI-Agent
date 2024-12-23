import tkinter as tk
from tkinter import messagebox, filedialog
import os
import hashlib

# Function to calculate the hash of a file
def calculate_file_hash(file_path, hash_algorithm):
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Function to calculate hash for all files in a folder
def calculate_folder_hash(folder_path, hash_algorithm):
    results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = calculate_file_hash(file_path, hash_algorithm)
                results.append((file, file_hash))
            except Exception as e:
                results.append((file, f"Error: {str(e)}"))
    return results

# Function to select a file and calculate its hash
def select_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    hash_algorithm = hash_var.get()
    try:
        file_hash = calculate_file_hash(file_path, hash_algorithm)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
        result_text.insert(tk.END, f"Algorithm: {hash_algorithm}\n")
        result_text.insert(tk.END, f"Hash: {file_hash}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to calculate hash: {str(e)}")

# Function to select a folder and calculate hashes for all files
def select_folder():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    hash_algorithm = hash_var.get()
    try:
        results = calculate_folder_hash(folder_path, hash_algorithm)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Folder: {folder_path}\n\n")
        for file, file_hash in results:
            result_text.insert(tk.END, f"{file}: {file_hash}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to calculate folder hashes: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("File Hash Calculator")
root.geometry("700x500")

# Dropdown for hash algorithm selection
hash_var = tk.StringVar(value="sha256")
algorithms = hashlib.algorithms_guaranteed
hash_label = tk.Label(root, text="Select Hash Algorithm:")
hash_label.pack(pady=5)
hash_dropdown = tk.OptionMenu(root, hash_var, *algorithms)
hash_dropdown.pack(pady=5)

# Button to select file
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)

# Button to select folder
folder_button = tk.Button(root, text="Select Folder", command=select_folder)
folder_button.pack(pady=10)

# Text box to display results
result_text = tk.Text(root, width=80, height=20)
result_text.pack(pady=5)

# Run the application
root.mainloop()
