import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random
from quiz_page import QuizPage
from data_entry import DataEntryPage

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.database = pd.read_csv("database.csv")
        self.terms = self.database['Term']
        self.definitions = self.database['Definition']

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.quiz_page_frame = tk.Frame(self.notebook)
        self.quiz_page = QuizPage(self.quiz_page_frame)

        self.data_entry_frame = tk.Frame(self.notebook)
        self.data_entry = DataEntryPage(self.data_entry_frame, self.database)

        self.notebook.add(self.quiz_page_frame, text="Quiz")
        self.notebook.add(self.data_entry_frame, text="Data Entry")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
