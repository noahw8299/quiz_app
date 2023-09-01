import tkinter as tk
from types import NoneType
import pandas as pd
import random
import subprocess
from tkinter import messagebox

class QuizPage:
    def __init__(self, parent, app, database):
        self.parent = parent
        self.app = app
        print(f"app {app}")
        self.database = pd.read_csv(database)
        self.terms = self.database["Term"]
        self.definitions = self.database["Definition"]
        print(self.definitions)
        self.current_language = "english"
        self.current_term = ""
        self.current_definition = ""
        self.correct_terms = None
        self.quiz_page_status = True

        self.show_quiz_page()

        if self.quiz_page_status:
            self.start_quiz()

    def show_quiz_page(self):
        print(f"showing quiz screen")
        self.title = tk.Label(self.parent, text="QUIZ YOURSELF\n", font=('helvetica', 18, 'bold'))
        self.title.pack()

        self.term_label = tk.Label(self.parent, text="Term", font=('helvetica', 30))
        self.term_label.pack()

        self.user_input = tk.Entry(self.parent)
        self.user_input.pack()
        self.user_input.bind("<Return>", self.check_answer)

        self.result_label = tk.Label(self.parent, text="", font=('helvetica', 18))
        self.result_label.pack()

        self.question_answered = False

    def start_quiz(self):
        self.correct_terms = set(self.definitions)
        print(f"self.correct_terms")
        self.next_question()

    def next_question(self):
        if not self.correct_terms:
            if self.current_language == "japanese":
                self.switch_language("english")
                print(f"switched language to {self.current_language}")
            messagebox.showinfo("Success", f"You completed all the terms!")
            self.quiz_page_status = False
            self.show_home_screen()

        if self.quiz_page_status:
            print(f"remaining terms: {self.correct_terms}, count: {len(self.correct_terms)}")

            # Select a random definition from the set of correct terms
            random_definition = random.choice(list(self.correct_terms))

            # Find the corresponding term for the randomly chosen definition
            self.current_term = self.terms[self.definitions == random_definition].values[0]
            self.current_definition = random_definition
            
            language = self.database.loc[self.database['Definition'] == self.current_definition, 'Language'].values[0]
            if self.current_language != language:
                self.switch_language(language)

            print(f"current language {self.current_language} term language {language}")
            self.term_label.config(text=f"{self.current_term} - {self.current_language}")
            self.user_input.delete(0, tk.END)
            self.user_input.focus()
            self.result_label.config(text="")
            self.question_answered = False

    def check_answer(self, event):
        user_input = self.user_input.get().strip().lower()

        if user_input == "":
            self.result_label.config(text="Enter definition")
        elif user_input == self.current_definition.strip().lower():
            self.result_label.config(text="Correct")
            # Remove the term from correct_terms
            self.correct_terms.discard(self.current_definition)

        else:
            self.result_label.config(text=f"Incorrect. The correct answer is {self.current_definition}")

        if not self.question_answered:
            self.question_answered = True
        else:
            self.clear_result()

    def clear_result(self):
        self.result_label.config(text="")
        self.next_question()

    def switch_language(self, language):
        try:
            # Use the osascript command to simulate pressing Control + Space
            subprocess.run(["osascript", "-e", 'tell application "System Events" to key code 49 using control down'])
            self.current_language = language
        except Exception as e:
            print("Error:", e)

    def clear_screan(self):
        print(f"clearing quiz screen")
        self.title.pack_forget()
        self.term_label.pack_forget()
        self.user_input.pack_forget()
        self.result_label.pack_forget()

    def show_home_screen(self):
        self.clear_screan()
        # Call the QuizApp's method to switch back to the home screen
        self.app.switch_to_home_screen()