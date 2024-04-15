import tkinter as tk
from tkinter import messagebox
import os

# Функция для запуска "Змейки"
def run_snake_game():
    os.system('python snake_game.py')

# Функция для запуска "Космических защитников"
def run_space_defenders():
    os.system('python space_defenders.py')

# Функция для запуска "шарика"
def run_turtle_game():
    os.system('python turtle.py')

root = tk.Tk()  # Creating instance of Tk class
root.title("Меню")
root.resizable(False, False)  # This code helps to disable windows from resizing


window_height = 200
window_width = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# # Создаем главное окно
# root = tk.Tk()
# root.title("Сборник игр")
# root.eval('tk::PlaceWindow . center')
#
#
# # Устанавливаем размеры и положение главного окна
# root.geometry("500x300")

tk.Label(text="Выберите игру", width=20, height=2).pack()

# Создаем кнопки для запуска игр
btn_snake = tk.Button(root, text="Змейка", command=run_snake_game)
btn_snake.pack(pady=7)

btn_space_defenders = tk.Button(root, text="Космические защитники", command=run_space_defenders)
btn_space_defenders.pack(pady=7)

btn_platformer = tk.Button(root, text="Шарик", command=run_turtle_game)
btn_platformer.pack(pady=7)

root.mainloop()
