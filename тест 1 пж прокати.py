import tkinter as tk
import random


class CenteredFixedSizeWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Тест")
        self.master.geometry("1280x720")
        self.master.resizable(width=False, height=False)
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - 1280) // 2
        y = (screen_height - 720) // 2
        self.master.geometry(f"1280x720+{x}+{y}")


class TestApp:
    def __init__(self, master):
        self.master = master
        # Задание параметров приложения
        self.master.title("Тест")
        self.questions_and_answers = {
            "Что означает HTML?": ["Гипертекстовый язык разметки", "Каскадные таблицы стилей", "Гипертекстовая метка",
                                   "Графический язык разметки"],
            "Какой тег используется для создания списка?": ["<list>", "<ul>", "<li>", "<ol>"],
            "Что означает атрибут 'href' в теге <a>?": ["Адрес ссылки", "Заголовок ссылки", "Текст ссылки",
                                                        "Оформление ссылки"],
            "Какой тег используется для создания заголовка?": ["<body>", "<h1>", "<title>", "<header>"],
            "Что такое CSS?": ["Каскадные таблицы стилей", "Гипертекстовая метка", "Язык программирования",
                               "HTML-фреймворк"]
        }
        self.correct_answers = ["Гипертекстовый язык разметки", "<list>", "Адрес ссылки", "<body>",
                                "Каскадные таблицы стилей"]
        self.index = 0
        self.correct_answers_count = 0
        self.question_label = tk.Label(master, text=list(self.questions_and_answers.keys())[self.index])
        self.question_label.pack()
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        self.shuffle_answers()

        for i in range(len(self.used_answers)):
            radio_button = tk.Radiobutton(master, text=self.used_answers[i], variable=self.radio_var,
                                          value=self.used_answers[i])
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(master, text="Ответить", command=self.check_answer)
        self.submit_button.pack()

    def shuffle_answers(self):
        self.used_answers = self.questions_and_answers[list(self.questions_and_answers.keys())[self.index]]
        random.shuffle(self.used_answers)

    def check_answer(self):
        selected_answer = self.radio_var.get()

        if selected_answer in self.correct_answers:
            self.correct_answers_count += 1

        self.index += 1
        if self.index < len(self.questions_and_answers):
            self.question_label.config(text=list(self.questions_and_answers.keys())[self.index])
            self.shuffle_answers()
            for i in range(len(self.used_answers)):
                self.radio_buttons[i].config(text=self.used_answers[i], value=self.used_answers[i])

        else:

            if self.index == len(
                    self.questions_and_answers) and selected_answer:  # Добавляем проверку, чтобы результат не изменялся при запуске
                score = 5
                results_window = tk.Toplevel()
                results_text = f"Правильных ответов: {self.correct_answers_count}\nОценка: {score} из 5"

                results_label = tk.Label(results_window, text=results_text)
                results_label.pack()
                close_button = tk.Button(results_window, text="Закрыть", command=results_window.destroy)
                close_button.pack()


root = tk.Tk()
app = TestApp(root)
app = CenteredFixedSizeWindow(root)
root.mainloop()
