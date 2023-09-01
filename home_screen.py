import tkinter as tk
import os
from quiz_page import QuizPage

class HomeScreen:
    def __init__(self, parent, app):
        self.parent = parent
        self.available_databases = self.find_available_databases()
        self.app = app
        self.quiz_page = None

        self.show_home_screen()
    
    def show_home_screen(self):
        print(f"showing home screen")
        self.title_label = tk.Label(self.parent, text="Welcome to Quiz App!\n\nSelect a Database:")
        self.title_label.pack()

        self.database_var = tk.StringVar(self.parent)
        self.database_var.set(self.available_databases[0])  # Set the default value

        self.database_menu = tk.OptionMenu(self.parent, self.database_var, *self.available_databases)
        self.database_menu.pack()

        self.start_button = tk.Button(self.parent, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

        self.learn_button = tk.Button(self.parent, text="Learn Terms", command=self.learn_terms)
        self.learn_button.pack()
        

    def find_available_databases(self):
        # Get the directory where your CSV databases are located
        database_directory = "./databases"

        # List all files in the directory
        all_files = os.listdir(database_directory)

        # Filter the list to include only CSV files
        csv_files = [filename for filename in all_files if filename.endswith(".csv")]

        return csv_files

    def start_quiz(self):
        selected_database = self.database_var.get()

        self.clear_screen()
        # create instance of quiz_page
        self.quiz_page = QuizPage(self.parent, self.app, f"databases/{selected_database}")

    def learn_terms(self):
        selected_database = self.database_var.get()

        self.clear_screen()
        # create instance of quiz_page
        self.quiz_page = QuizPage(self.parent, self.app, f"databases/{selected_database}")
    
    def clear_screen(self):
        print(f"clearing home screen")
        # Hide the HomeScreen elements and display the QuizPage elements
        self.title_label.pack_forget()
        self.database_menu.pack_forget()
        self.start_button.pack_forget()
        self.learn_button.pack_forget()
        