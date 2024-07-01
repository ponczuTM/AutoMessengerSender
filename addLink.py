import json
import tkinter as tk
from tkinter import messagebox, filedialog

def collect_messenger_links():
    links = []
    
    def add_link():
        link = link_entry.get().strip()
        if link:
            links.append(link)
            link_entry.delete(0, tk.END)
            listbox.insert(tk.END, link)
        else:
            messagebox.showerror("Error", "Please enter a valid link.")

    def remove_link():
        selected_index = listbox.curselection()
        if selected_index:
            links.pop(selected_index[0])
            listbox.delete(selected_index)

    def finish_input():
        link_input_window.destroy()

    link_input_window = tk.Tk()
    link_input_window.title("Collect Messenger Links")
    link_input_window.configure(bg='#222831')

    # Custom style for entry fields
    entry_style = {'bg': '#30475e', 'fg': '#ffffff', 'borderwidth': 0, 'highlightthickness': 0}

    tk.Label(link_input_window, text="Enter your Messenger links below:", bg='#222831', fg='#ffffff').pack(padx=10, pady=10)

    entry_frame = tk.Frame(link_input_window, bg='#30475e', padx=10, pady=5)
    entry_frame.pack(padx=10, pady=5)
    link_entry = tk.Entry(entry_frame, width=50, **entry_style)
    link_entry.pack(fill=tk.BOTH, expand=True)

    add_button = tk.Button(link_input_window, text="Add Link", command=add_link, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0)
    add_button.pack(padx=10, pady=5)

    remove_button = tk.Button(link_input_window, text="Remove Selected Link", command=remove_link, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0)
    remove_button.pack(padx=10, pady=5)

    listbox = tk.Listbox(link_input_window, width=70, height=10, bg='#30475e', fg='#ffffff', borderwidth=0, highlightthickness=0)
    listbox.pack(padx=10, pady=10)

    finish_button = tk.Button(link_input_window, text="Finish", command=finish_input, bg='#30475e', fg='#ffffff', relief=tk.FLAT, padx=10, pady=5, borderwidth=0, highlightthickness=0)
    finish_button.pack(padx=10, pady=10)

    link_input_window.mainloop()

    return links

def save_links_to_file(links, filename="messenger_links.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(links, file, indent=4)
        messagebox.showinfo("Information", f"Messenger links have been saved in {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the links: {str(e)}")

def main():
    links = collect_messenger_links()
    if links:
        save_links_to_file(links)

if __name__ == "__main__":
    main()
