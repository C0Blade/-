from tkinter import *
import json
from tkinter import messagebox

import requests

def get_file():
    global saved_file
    global get_file1
    username = username_entry.get()
    url = f"https://api.github.com/users/{username}"
    get_file1 = requests.get(url)
    with open('data_git.json', 'w') as saved_file:
        json.dump(get_file1.json(), saved_file)
        if get_file1.status_code == 200:
            messagebox.showinfo("Успешно", "Файл из введённого репозитория был получен")
        elif get_file1.status_code != 200:
            messagebox.showerror("Ошибка",
                                 "Введено неверное имя репозитория, или файл не может быть получен")

def load_file():
    with open('data_git.json', 'r') as saved_file:
        data = json.load(saved_file)
        info = {
            'company': (data["company"]),
            'created_at': (data["created_at"]),
            'email': (data["email"]),
            'id': (data["id"]),
            'name': (data["name"]),
            'url': (data["url"])
        }
        with open('data_git.json', 'w') as filtered_file:
            json.dump(info, filtered_file)
        messagebox.showinfo("Успешно", "Нужные данные были записаны в файл")

okno = Tk()
okno.title("Зинченко Кирилл Русланович")
okno.geometry("800x600+550+200")
okno.resizable(False, False)

username_entry = Entry(okno)
username_entry.pack()
file_button = Button(okno, text="Получить файл c репозитория", command=get_file)
file_button.pack()
file2_button = Button(okno, text="Записать данные в файл", command=load_file)
file2_button.pack()

okno.mainloop()