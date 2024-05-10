import tkinter as tk
from tkinter import messagebox

class HtmlCssTest(tk.Tk):
    def __init__(self, questions, answers):
        super().__init__()

        self.questions = questions
        self.answers = answers
        self.correct_answers = ["Гипертекстовый язык разметки", "<list>", "Адрес ссылки", "<body>", "аскадные таблицы"]

        self.score = 0
        self.current_question = 0

        self.label = tk.Label(self, text=self.questions[self.current_question])
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=5)

    def submit_answer(self):
        user_answer = self.entry.get().strip().lower()
        if user_answer == self.correct_answers[self.current_question].lower():
            self.score += 1
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question])
            self.entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Результат", f"Вы набрали {self.score} из {len(self.questions)} очков.")

html_css_test = HtmlCssTest(["Что означает HTML?", "Какой тег используется для создания списка?",
                             "Что означает атрибут 'href' в теге <a>?", "Какой тег используется для создания заголовка?",
                             "Что такое CSS?"],
                           [["Гипертекстовый язык разметки", "Каскадные таблицы стилей", "Гипертекстовая метка", "Графический язык разметки"],
                            ["<list>", "<ul>", "<li>", "<ol>"],
                            ["Адрес ссылки", "Заголовок ссылки", "Текст ссылки", "Оформление ссылки"],
                            ["<body>", "<h1>", "<title>", "<header>"],
                            ["Каскадные таблицы стилей", "Гипертекстовая метка", "Язык программирования", "HTML-фреймворк"]])

html_css_test.title("HTML/CSS Тест")
html_css_test.geometry("400x200")
html_css_test.mainloop()