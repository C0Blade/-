import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Функция для калькулятора
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = combobox.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Ошибка деления"
        else:
            result = "Неверная операция"
        calc_result_label.config(text=f"Результат: {result}")
    except ValueError:
        calc_result_label.config(text="Ошибка: введите числа!")

# Функция для чекбоксов
def check_option():
    if var1.get():
        choice = "Вы выбрали первый вариант"
    elif var2.get():
        choice = "Вы выбрали второй вариант"
    elif var3.get():
        choice = "Вы выбрали третий вариант"
    else:
        choice = "Вы ничего не выбрали"
    messagebox.showinfo("Результат", choice)

# Функция для загрузки текста из файла
def load_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, text_content)

# Создание окна
app = tk.Tk()
app.title("Зинченко Кирилл Русланович")
app.geometry("500x400")

# Создание вкладок
notebook = ttk.Notebook(app)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Первая вкладка - калькулятор
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

entry1 = ttk.Entry(tab1, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

combobox = ttk.Combobox(tab1, values=["+", "-", "*", "/"], width=5)
combobox.set("+")
combobox.grid(row=0, column=1, padx=5, pady=5)

entry2 = ttk.Entry(tab1, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

calc_button = ttk.Button(tab1, text="Рассчитать", command=calculate)
calc_button.grid(row=0, column=3, padx=5, pady=5)

calc_result_label = ttk.Label(tab1, text="Результат: ")
calc_result_label.grid(row=1, column=0, columnspan=4, pady=5)

# Вторая вкладка - чекбоксы
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Выбор")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = ttk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(anchor="w", padx=10, pady=5)

checkbox2 = ttk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(anchor="w", padx=10, pady=5)

checkbox3 = ttk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(anchor="w", padx=10, pady=5)

check_button = ttk.Button(tab2, text="Проверить", command=check_option)
check_button.pack(pady=10)

# Третья вкладка - работа с текстом
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Работа с текстом")

menu = tk.Menu(app)
app.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text)

text_widget = tk.Text(tab3, wrap="word", height=15)
text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Запуск приложения
app.mainloop()