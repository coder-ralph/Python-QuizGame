import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.question_index = 0
        self.score = 0

        # Question data
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Madrid", "London", "Berlin"],
                "answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Mars", "Saturn", "Earth"],
                "answer": "Jupiter"
            },
            {
                "question": "Which programming language is used to build webpages?",
                "options": ["Python", "Java", "HTML", "C++"],
                "answer": "HTML"
            },

            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "answer": "Tokyo"
            },
            {
                "question": "Who is the CEO of Tesla?",
                "options": ["Elon Musk", "Jeff Bezos", "Bill Gates", "Mark Zuckerberg"],
                "answer": "Elon Musk"
            },
            {
                "question": "Which programming language is known as the 'mother of all languages'?",
                "options": ["Python", "C", "Java", "Assembly"],
                "answer": "Assembly"
            },
            # Add more questions here
        ]

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="Question")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack()

        self.next_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.config(text=question["question"])
            random.shuffle(question["options"])
            for i in range(4):
                self.option_buttons[i].config(text=question["options"][i])
            self.question_index += 1
        else:
            messagebox.showinfo("Quiz Game", f"Quiz completed!\nYour score is: {self.score}")
            self.root.destroy()

    def check_answer(self, button_index):
        question = self.questions[self.question_index - 1]
        selected_option = question["options"][button_index]
        if selected_option == question["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

root = tk.Tk()
app = QuizGame(root)
root.mainloop()
