from tkinter import *
from datetime import datetime

#Константы

BG_COLOR = '#9bd5d3'
FONT = "Times"

# Глобальные переменные

temp = 0 # количество секунд с момента старта таймера
after_id = '' # будет хранить идентификатор, возвращаемый методом after



'''Функция tick для работы с глобальными переменными. Значение global означает, что все
 значения, которые мы будем присваивать этим переменным у нас будут видны вне 
 функции(за пределами функции tick). Таймер - это непрерывно увеличивающаяся 
 последовательность цифр, которая в отформатированном виде, будет циклически 
 отображаться в виджете. Цикл должен быть бесконечным. В графических приложениях
 использовать бесконечные циклы нельзя, поэтому мы можем вызвать метод after, для
 главного окна root, который принимает два аргумента: время в миллисекундах и 
 функция, которую нужно выполнить через указанное время. Т.е. мы будем 1 раз 
 в секунду увеличивать счетчик на единицу. Так же метод after возвращает 
 идентификатор, который позволяет остановить отсчет в дальнейшем.
 Запись datetime.fromtimestamp(TEMP) возвращает дату, соответствующую количеству 
 секунд, прошедших с начала эпохи. А дополнение strftime("%M:%S") возвращает 
 форматированную строку
'''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)  # 1000 миллисекунд = 1 секунда
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    timer_label.configure(text = str(f_temp)) # для проверки промежуточного значения
                                       # выводим TEMP c помощью метода configure
    temp += 1                          # переменная TEMP увеличивается на единицу


'''Функция для кнопки "Старт". Функция будет запускать таймер, прятать кнопку
"Старт", и отображать кнопку "Стоп". Чтобы удалить кнопку "Старт" удаляем
виджет и всю информацию о его расположении из упаковщика при помощи метода
grid_forget. btn2.grid будет размещать кнопку "Стоп", в освободившемся месте'''

def start_sw():
    start_button.grid_forget()
    stop_button.grid(row = 1, columnspan = 2, sticky = "ew")
    tick()

'''Функция для кнопки "Стоп". При нажатии на кнопку "Стоп" кнопка будет исчезать
, а на ее месте будет появляться две кнопки "Продолжить" и "Сбросить". 
root.after_cancel(AFTER_ID) - завершает цикл after, который запускается при
вызове функции tick'''

def stop_sw():
    stop_button.grid_forget()
    continue_button.grid(row = 1, column = 0, sticky = "ew")
    reset_button.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)


'''Функция для кнопки "Продолжить". '''

def continue_sw():
    continue_button.grid_forget() # Прячем кнопку
    reset_button.grid_forget() # Прячем кнопку
    stop_button.grid(row=1, columnspan=2, sticky="ew") # Отображаем кнопку "Старт"
    tick() # Вызываем функцию tick

'''Функция для кнопки "Сбросить". В этой функции мы сбрасываем счетчик секунд temp
, поэтому объявляем глобальную переменную temp и сбрасываем ее присваивая значение 0'''

def reset_sw():
    global temp # Объявляем переменную глобальной
    temp = 0 # Сбрасываем переменную
    timer_label.configure(text = "00:00") # Задаем текст для переменной TEMP
    continue_button.grid_forget() # Прячем кнопку
    reset_button.grid_forget() # Прячем кнопку
    start_button.grid(row=1, columnspan=2, sticky="ew") # Отображаем кнопку "Старт"



# Окно таймера

root = Tk() # Создаем корневое окно
root.title('Timer') # Задаем окну название

timer_label = Label(root, width = 5, font = (FONT, 250), text = "00:00", bg = BG_COLOR)
timer_label.grid(row = 0, columnspan = 2) # Параметр columnspan задает сколько столбцов будет занимать виджет
# grid - упаковщик


# Создаем кнопки по состоянию таймера
# 1 состояние, когда он еще не запущен, при этом видна 1 кнопка "Старт"
# 2 состояние, когда таймер запущен и видна кнопка "Стоп"
# 3 состояние, когда таймер остановлен в этом случае видны две кнопки
# "Продолжить" и "Сбросить"

start_button = Button(root, text = "Старт", font = (FONT, 50), command = start_sw)
stop_button = Button(root, text = "Стоп", font = (FONT, 50), command = stop_sw)
continue_button = Button(root, text = "Продолжить", font = (FONT, 50), command = continue_sw)
reset_button = Button(root, text = "Сбросить", font = (FONT, 50), command = reset_sw)

start_button.grid(row = 1, columnspan = 2, sticky = "ew")






root.mainloop()