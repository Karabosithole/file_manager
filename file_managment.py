import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Management System")
        self.master.geometry("600x400")

        # Frame for file list
        self.file_frame = tk.Frame(self.master)
        self.file_frame.pack(pady=10)

        self.file_listbox = tk.Listbox(self.file_frame, width=50, height=15)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.file_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.file_listbox.yview)

        # Buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        self.browse_button = tk.Button(self.button_frame, text="Browse", command=self.browse)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        self.create_button = tk.Button(self.button_frame, text="Create File", command=self.create_file)
        self.create_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete File", command=self.delete_file)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.rename_button = tk.Button(self.button_frame, text="Rename File", command=self.rename_file)
        self.rename_button.pack(side=tk.LEFT, padx=5)

        self.path = ""

    def browse(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.file_listbox.delete(0, tk.END)  # Clear previous entries
            for file in os.listdir(self.path):
                self.file_listbox.insert(tk.END, file)  # Insert files into listbox

    def create_file(self):
        if self.path:
            file_name = "new_file.txt"  # Default name
            full_path = os.path.join(self.path, file_name)
            with open(full_path, 'w') as f:
                f.write("")  # Create an empty file
            self.browse()  # Refresh file list

    def delete_file(self):
        selected_file = self.file_listbox.curselection()
        if selected_file:
            file_name = self.file_listbox.get(selected_file)
            full_path = os.path.join(self.path, file_name)
            os.remove(full_path)
            self.browse()  # Refresh file list

    def rename_file(self):
        selected_file = self.file_listbox.curselection()
        if selected_file:
            file_name = self.file_listbox.get(selected_file)
            new_name = filedialog.asksaveasfilename(initialfile=file_name)
            if new_name:
                full_path = os.path.join(self.path, file_name)
                os.rename(full_path, new_name)
                self.browse()  # Refresh file list

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
