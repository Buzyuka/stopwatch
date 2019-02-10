import os
import tkinter

#Константы
IMG_PATH = 'img'
WIDTH = 700
HEIGHT = 450
BG_COLOR = '#9bd5d3'


# События для мышки
def mouse_click(event):
    print(event.num, event.x, event.y)
'''Задаем координаты при клике мыши, и номер клавиши клика'''




root = tkinter.Tk() # Создаем корневое окно
root.title('Timer') # Задаем окну название
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)#Задаем окну параметры
canvas.pack()
canvas.bind('<Button-1>', mouse_click) # Левая кнопка мыши
canvas.bind('<Button-2>', mouse_click, '+') # Колесико
canvas.bind('<Button-3>', mouse_click, '+') # Правая кнопка мыши

files = sorted(os.listdir(IMG_PATH)) # Прописываем путь к директории с нашими файлами

images = []
for name in files:
    rel_path = os.path.join(IMG_PATH, name)
    print(rel_path)
    image = tkinter.PhotoImage(file = rel_path)




root.mainloop()