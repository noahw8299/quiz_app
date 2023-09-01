import tkinter as tk
from tkinter import messagebox
import pandas as pd

class DataEntryPage:
    def __init__(self, parent, database):
        self.parent = parent
        self.database = database
        self.terms = self.database['Term']
        self.definitions = self.database['Definition']

        self.new_set = tk.Button(self.parent, text="Create New Study Set", command=self.show_data_entry)
        self.new_set.pack(side="top", pady=10, anchor="center")

        self.edit_set = tk.Button(self.parent, text="Edit Existing Study Set", command=self.edit_data)
        self.edit_set.pack(side="top", pady=10, anchor="center")

    
    def show_data_entry(self):
        self.unpack_init()
        self.term_label = tk.Label(self.parent, text="DATA ENTRY\n")
        self.term_label.pack()

        self.set_label = tk.Label(self.parent, text="Study Set Name")
        self.set_label.pack()

        self.set_name = tk.Entry(self.parent)
        self.set_name.pack()

        self.submit = tk.Button(self.parent, text="Submit", command=self.set_title)
        self.submit.pack()

        # self.term_label = tk.Label(self.parent, text="Term")
        # self.term_label.pack()

        # self.new_vocab = tk.Entry(self.parent)
        # self.new_vocab.pack()

        # self.definition_label = tk.Label(self.parent, text="Definition:")
        # self.definition_label.pack()

        # self.new_def = tk.Entry(self.parent)
        # self.new_def.pack()

        # self.language_var = tk.StringVar(self.parent)
        # self.language_var.set('english')  # Set the default value

        # self.lang_menu = tk.OptionMenu(self.parent, self.language_var, 'english', 'japanese')
        # self.lang_menu.pack()

        # self.new_term = tk.Button(self.parent, text="Add New Term", command=self.add_new_term)
        # self.new_term.pack()

        # self.save_button = tk.Button(self.parent, text="Save", command=self.save_data)
        # self.save_button.pack()

    def save_data(self):
        new_term = self.new_vocab.get().strip()
        new_definition = self.new_def.get().strip()

        if new_term and new_definition:
            new_term = {"Term": new_term, "Definition": new_definition}
            new_term = pd.DataFrame(new_term, index=[0])

            self.database = pd.concat([self.database, new_term], ignore_index=True)
            self.database.to_csv("database.csv", index = False)

            messagebox.showinfo("Success", f"{new_term} saved!")

            self.new_vocab.delete(0, tk.END)
            self.new_def.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both term and definition are required.")

    def edit_data(self):
        self.title = tk.Label(self.parent, text="EDIT DATA")
        self.title.pack()

    def unpack_init(self):
        self.new_set.pack_forget()
        self.edit_set.pack_forget()

    def add_new_term(self):
        print("add_new_term")

    def set_title(self):
        print("set title")
