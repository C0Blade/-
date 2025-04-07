from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Основное окно
window = Tk()
window.title("Зинченко Кирилл Русланович")
window.geometry("400x300")
window.resizable(False, False)

# Вкладки
notebook = ttk.Notebook(window)
notebook.pack(fill=BOTH, expand=True)

calc_frame = Frame(notebook)
check_frame = Frame(notebook)
text_frame = Frame(notebook)

calc_frame.config(bg="gray")
check_frame.config(bg="#0010A1")

notebook.add(calc_frame, text='Калькулятор')
notebook.add(check_frame, text='Чекбоксы')
notebook.add(text_frame, text='Текст')

# Работа с первой вкладкой (калькулятор)
# Функция для калькулятора
def calculation():
    try:
        numb1 = float(calc_entry_numb1.get())
        numb2 = float(calc_entry_numb2.get())
        op = ops_calc.get()
        if op == '+':
            result = numb1 + numb2
        elif op == '-':
            result = numb1 - numb2
        elif op == '*':
            result = numb1 * numb2
        elif op == '/':
            result = numb1 / numb2
            if result == 0:
               raise ZeroDivisionError
        messagebox.showinfo("Результат", f"{result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа!")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "На ноль делить нельзя!")

# Первое окно ввода числа для калькулятора
calc_entry_numb1 = ttk.Entry(calc_frame)
calc_entry_numb1.pack(side=LEFT)

# Список операций
ops = ["+", "-", "*", "/"]
ops_calc = StringVar()
ops_calc.set(ops[0])
droplist = OptionMenu(calc_frame, ops_calc, *ops)
droplist.pack(side=LEFT)

# Второе окно ввода числа для калькулятора
calc_entry_numb2 = ttk.Entry(calc_frame)
calc_entry_numb2.pack(side=LEFT)

# Кнопка равно, вызов функции
result_button = Button(calc_frame, text="=", command=calculation)
result_button.pack(side=LEFT)

# Работа с второй вкладкой
# Функция
def checkboxes():
    choices = []
    if checked1.get() == 1:
        choices.append("первого")
    if checked2.get() == 1:
        choices.append("второго")
    if checked3.get() == 1:
        choices.append("третьего")
    if choices:
        messagebox.showinfo("Ваш выбор", f"Состоит из: {choices} варианта")
    else:
        messagebox.showerror("Ошибка", "Вы ничего не выбрали")

# Переменные для проверки прожат ли чекбокс
checked1 = IntVar()
checked2 = IntVar()
checked3 = IntVar()

# Создание чекбокса
box1 = Checkbutton(check_frame, text="Первый", bg="#0010A1", fg='yellow', variable=checked1)
box2 = Checkbutton(check_frame, text="Второй", bg="#0010A1", fg='yellow', variable=checked2)
box3 = Checkbutton(check_frame, text="Третий", bg="#0010A1", fg='yellow', variable=checked3)

#Размещение виджета чекбокса
box1.pack(anchor=NW)
box2.pack(anchor=NW)
box3.pack(anchor=NW)

# Кнопка показа выбора
check_button = Button(check_frame, text="Показ выбора",  bg = "blue", fg="yellow", command=checkboxes)
check_button.pack(anchor=NW)

# Третья вкладка
# Функция для работы с файлами
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_field.delete(1.0, END)  # Очистить текстовое поле
            text_field.insert(END, text)  # Вставить текст из файла

# Добавление кнопки работы с текстом
text_button =  Button(text_frame, text = "Загрузить текстовый файл", bg = "green", fg="white", command=upload_file)
text_button.pack(fill=X)

# Текстовое поле
text_field = Text(text_frame, wrap=WORD, bg='black', fg='white')
text_field.pack()

window.mainloop()