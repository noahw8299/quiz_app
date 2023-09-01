import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random
from quiz_page import QuizPage
from data_entry import DataEntryPage
from home_screen import HomeScreen

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.database = pd.read_csv("databases/genki II kanji.csv")
        self.terms = self.database['Term']
        self.definitions = self.database['Definition']

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.home_page_frame = tk.Frame(self.notebook)
        self.home_page = HomeScreen(self.home_page_frame, self)

        self.data_entry_frame = tk.Frame(self.notebook)
        self.data_entry = DataEntryPage(self.data_entry_frame, self.database)

        self.notebook.add(self.home_page_frame, text="Home Screen")
        self.notebook.add(self.data_entry_frame, text="Data Entry")
    
    def switch_to_home_screen(self):
        print(f"switing to home screen")
        self.notebook.select(self.home_page_frame)
        # Reinitialize the HomeScreen instance
        self.home_page = HomeScreen(self.home_page_frame, self)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.home_page.app = app
    root.mainloop()
