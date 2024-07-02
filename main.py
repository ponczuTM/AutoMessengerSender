import json
import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time

def add_link():
    link = link_entry.get().strip()
    if link:
        links.append(link)
        link_entry.delete(0, tk.END)
        listbox.insert(tk.END, link)
    else:
        messagebox.showerror("Error", "Please enter a valid link.")

def load_links_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read().strip()
                new_links = file_content.split(',')
                links.extend(new_links)
                for link in new_links:
                    listbox.insert(tk.END, link)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the links: {str(e)}")

def remove_link():
    selected_index = listbox.curselection()
    if selected_index:
        links.pop(selected_index[0])
        listbox.delete(selected_index)

def finish_input():
    global links
    link_input_window.destroy()

def save_links_to_file():
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        try:
            with open(filename, 'w') as file:
                json.dump(links, file, indent=4)
            messagebox.showinfo("Information", f"Messenger links have been saved in {filename}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the links: {str(e)}")

def browse_json_file():
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    json_entry.delete(0, tk.END)
    json_entry.insert(0, filename)

def browse_message_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    message_entry.delete(0, tk.END)
    message_entry.insert(0, filename)

def load_links_from_json(filename):
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
        # pyautogui.hotkey('ctrl', 'a')
        # time.sleep(0.2)
        # pyautogui.press('delete')
        time.sleep(0.2)
        for link in links:
            pyautogui.hotkey('ctrl', 't')
            time.sleep(1)
            pyautogui.write(link)
            time.sleep(1)
            pyautogui.press('enter')  # Press "Enter" after each link
            time.sleep(7)
            pyautogui.write(message)
            pyautogui.press('enter')
            time.sleep(1)
            # pyautogui.click()
            # pyautogui.click()
            # pyautogui.hotkey('ctrl', 'a')
            # time.sleep(0.2)
            # pyautogui.press('delete')
            # time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.4)

def start_typing():
    filename = json_entry.get()
    message_file = message_entry.get()

    if not filename:
        messagebox.showerror("Error", "Please select a JSON file.")
        return
    
    links = load_links_from_json(filename)
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

# Collecting Messenger links section
links = []

tk.Label(app, text="Enter your Messenger links below:", bg='#222831', fg='#ffffff', font=('Arial', 12)).grid(row=0, column=0, columnspan=3, padx=10, pady=10)

entry_frame = tk.Frame(app, bg='#e6e6e6', padx=50, pady=5)
entry_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
link_entry = tk.Entry(entry_frame, width=150, bg='#e6e6e6', fg='#000000', borderwidth=0, highlightthickness=0)
link_entry.pack(fill=tk.BOTH, expand=True)

tk.Button(app, text="Add Link", command=add_link, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=100, pady=10, borderwidth=0, highlightthickness=0).grid(row=2, column=0, padx=10, pady=5)
tk.Button(app, text="Load Links from File", command=load_links_from_file, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=100, pady=10, borderwidth=0, highlightthickness=0).grid(row=2, column=1, padx=10, pady=5)
tk.Button(app, text="Remove Selected Link", command=remove_link, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=100, pady=10, borderwidth=0, highlightthickness=0).grid(row=2, column=2, padx=10, pady=5)

listbox = tk.Listbox(app, width=130, height=10, bg='#30475e', fg='#ffffff', borderwidth=0, highlightthickness=0)
listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

tk.Button(app, text="Save", command=save_links_to_file, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# JSON file entry
tk.Label(app, text="Select JSON file with links:", bg='#222831', fg='#ffffff', font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10)
json_entry = tk.Entry(app, width=50, bg='#30475e', fg='#ffffff', borderwidth=0, highlightthickness=0)
json_entry.grid(row=5, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_json_file, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0).grid(row=5, column=2, padx=10, pady=10)

# Text file entry
tk.Label(app, text="Select text file with message:", bg='#222831', fg='#ffffff', font=('Arial', 12)).grid(row=6, column=0, padx=10, pady=10)
message_entry = tk.Entry(app, width=50, bg='#30475e', fg='#ffffff', borderwidth=0, highlightthickness=0)
message_entry.grid(row=6, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_message_file, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0).grid(row=6, column=2, padx=10, pady=10)

# Start typing button
tk.Button(app, text="Start typing", command=start_typing, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0).grid(row=7, column=0, columnspan=3, pady=20)

# Launch main loop
app.mainloop()
