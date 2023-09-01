import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.database = pd.read_csv("database.csv")
        self.terms = self.database['Term']
        self.definitions = self.database['Definition']

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.quiz_page = self.create_quiz_page()
        self.data_entry_page = self.create_data_entry_page()

        self.notebook.add(self.quiz_page, text="Quiz")
        self.notebook.add(self.data_entry_page, text="Data Entry")

    def create_quiz_page(self):
        quiz_page = tk.Frame(self.notebook)

        self.term_label = tk.Label(quiz_page, text="")
        self.term_label.pack()

        self.user_input = tk.Entry(quiz_page)
        self.user_input.pack()
        self.user_input.bind("<Return>", self.check_answer)

        self.result_label = tk.Label(quiz_page, text="")
        self.result_label.pack()

        self.question_answered = False
        self.next_question()

        return quiz_page

    def create_data_entry_page(self):
        data_entry_page = tk.Frame(self.notebook)

        term_label = tk.Label(data_entry_page, text="Term:")
        term_label.pack()

        self.term_entry = tk.Entry(data_entry_page)
        self.term_entry.pack()

        definition_label = tk.Label(data_entry_page, text="Definition:")
        definition_label.pack()

        self.definition_entry = tk.Entry(data_entry_page)
        self.definition_entry.pack()

        save_button = tk.Button(data_entry_page, text="Save", command=self.save_data)
        save_button.pack()

        return data_entry_page

    def next_question(self):
        random_number = random.randint(0, len(self.terms) - 1)
        self.current_term = self.terms[random_number]
        self.current_definition = self.definitions[random_number]

        self.term_label.config(text=self.current_term)
        self.user_input.delete(0, tk.END)
        self.user_input.focus()
        self.result_label.config(text="")
        self.question_answered = False

    def check_answer(self, event):
        user_input = self.user_input.get().strip()

        if user_input == "":
            self.result_label.config(text="Enter definition")
        elif user_input == self.current_definition:
            self.result_label.config(text="Correct")
        else:
            self.result_label.config(text=f"Incorrect. The correct answer is {self.current_definition}")

        if not self.question_answered:
            self.question_answered = True
        else:
            self.clear_result()

    def clear_result(self):
        self.result_label.config(text="")
        self.next_question()

    def save_data(self):
        new_term = self.term_entry.get().strip()
        new_definition = self.definition_entry.get().strip()

        if new_term and new_definition:
            new_term = {"Term": new_term, "Definition": new_definition}
            new_term = pd.DataFrame(new_term, index=[0])

            self.database = pd.concat([self.database, new_term], ignore_index=True)
            self.database.to_csv("database.csv", index = False)

            messagebox.showinfo("Success", "Data saved successfully!")

            self.term_entry.delete(0, tk.END)
            self.definition_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Both term and definition are required.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()