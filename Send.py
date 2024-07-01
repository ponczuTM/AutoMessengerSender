import json
import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time

def load_links_from_file(filename):
    try:
        with open(filename, 'r') as file:
            links = json.load(file)
        return links
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", f"JSON decoding error in file {filename}.")
        return []

def remove_https_prefix(links):
    return [link.replace("https://", "") for link in links]

def type_links(links, message):
    if not links:
        messagebox.showerror("Error", "No links to type.")
    else:
        messagebox.showinfo("Information", "Click in the input field where you want to type the links. You have 7 seconds.")
        time.sleep(7)  # Wait for user to click in input field
        for link in links:
            pyautogui.typewrite(link)
            time.sleep(1)
            pyautogui.press('enter')  # Press "Enter" after each link
            time.sleep(7)
            pyautogui.write(message)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.click()  # Left click after sending message

def browse_json_file():
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    json_entry.delete(0, tk.END)
    json_entry.insert(0, filename)

def browse_message_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    message_entry.delete(0, tk.END)
    message_entry.insert(0, filename)

def start_typing():
    filename = json_entry.get()
    message_file = message_entry.get()

    if not filename:
        messagebox.showerror("Error", "Please select a JSON file.")
        return
    
    links = load_links_from_file(filename)
    links = remove_https_prefix(links)
    
    if not links:
        messagebox.showerror("Error", "No links found in the JSON file.")
        return

    if not message_file:
        messagebox.showerror("Error", "Please select a text file for the message.")
        return

    with open(message_file, 'r') as file:
        message = file.read().strip()

    type_links(links, message)

# Main window creation
app = tk.Tk()
app.title("Auto Typer")
app.configure(bg='#222831')  # Background color for the main window

# Widget styles
widget_style = {
    'bg': '#31363F',  # Background color for input fields and text
    'fg': '#ffffff',
    'font': ('Arial', 12),
    'borderwidth': 0,
    'highlightthickness': 0,
}

# JSON file entry
tk.Label(app, text="Select JSON file with links:", bg='#222831', fg='#ffffff', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10)
json_entry = tk.Entry(app, width=50, **widget_style)
json_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_json_file, **widget_style).grid(row=0, column=2, padx=10, pady=10)

# Text file entry
tk.Label(app, text="Select text file with message:", bg='#222831', fg='#ffffff', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Entry(app, width=50, **widget_style)
message_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_message_file, **widget_style).grid(row=1, column=2, padx=10, pady=10)

# Start typing button
tk.Button(app, text="Start typing", command=start_typing, **widget_style).grid(row=2, column=0, columnspan=3, pady=20)

# Launch main loop
app.mainloop()
