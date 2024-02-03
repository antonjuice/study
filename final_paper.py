'''UI программа сортировки списка'''

from time import perf_counter_ns
from tkinter import (
    Tk, Frame, Button, Entry, Label, ttk,
    messagebox as box)


def output_message(type_msg: str, msg: str):
    '''Вывод информации во всплывающем окне.
    
    Параметр `type`:
    - `msg` - информационное сообщение;
    - `err` - ошибка.

    Cообщение передается в параметре `info`.
    '''

    match type_msg:
        case 'info':
            box.showinfo('Информация', msg)
        case 'err':
            box.showerror('Ошибка', msg)


def bubble_sort(lst: list) -> str:
    '''Сортировка пузырьком'''

    for _ in range(len(lst)-1):
        for i in range(0, len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst


def heapify(lst: list, size: int, indx: int):
    '''Преобразование в двоичную кучу (для пирамидальной сортировки)
    
    - `lst` - список элементов;
    - `size` - размер кучи;
    - `indx` - корневой индекс.'''

    largest = indx
    left = 2 * indx + 1
    right = 2 * indx + 2

    if left < size and lst[indx] < lst[left]:
        largest = left
    if right < size and lst[largest] < lst[right]:
        largest = right
    if largest != indx:
        lst[indx], lst[largest] = lst[largest], lst[indx]
        heapify(lst=lst, size=size, indx=largest)


def pyramid_sort(lst: list) -> list:
    '''Пирамидальная сортировка'''

    lst_len = len(lst)

    for i in range(lst_len, -1, -1):
        heapify(lst=lst, size=lst_len, indx=i)

    for j in range(lst_len-1, 0, -1):
        lst[j], lst[0] = lst[0], lst[j]
        heapify(lst=lst, size=j, indx=0)

    return lst


def merge_sort(lst: list) -> list:
    '''Сортировка слиянием'''

    if len(lst) > 1:
        x, y, z = 0, 0, 0
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]

        merge_sort(left)
        merge_sort(right)

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                lst[z] = left[x]
                x += 1
            else:
                lst[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            lst[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            lst[z] = right[y]
            y += 1
            z += 1

    return lst


def quick_sort(lst: list) -> list:
    '''Быстрая ортировка'''

    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left, right = [], []

        for elem in lst[1:]:
            if elem < pivot:
                left.append(elem)
            else:
                right.append(elem)

        return quick_sort(left) + [pivot] + quick_sort(right)


def check_input(inp: str) -> list:
    '''Проверка введенных значений.
    
    Если проверка успешная, возвращается список элементов'''

    if not inp:
        output_message(type_msg='err', msg='Не введена последовательность чисел')
        return False

    inp = inp.replace(' ', '')
    lst_check = inp.split(',')
    lst = []

    for i in lst_check:
        try:
            int(i)
        except ValueError:
            output_message(type_msg='err', msg='Элементы должны быть числами')
            return False
        lst.append(int(i))

    if len(lst) == 1:
        output_message(type_msg='err', msg='Зачем сортировать 1 элемент?')
        return False

    return lst


SORT_TYPES = {
    'Пузырьком': bubble_sort,
    'Пирамидальная': pyramid_sort,
    'Слиянием': merge_sort,
    'Быстрая': quick_sort
}


def input_processing():
    '''Обработка пользовательского ввода'''

    inp = entry_input.get()
    sort = cobmo_list.get()

    if not sort:
        output_message(type_msg='err', msg='Не выбран вариант сортировки')
        return

    result_lst = check_input(inp)
    if result_lst:
        start_time = perf_counter_ns()
        sorted_lst = SORT_TYPES[sort](result_lst)
        finish_time = perf_counter_ns()
        result_time = (finish_time - start_time) / 1_000_000
        message = ', '.join(str(s) for s in sorted_lst)
        output_message(type_msg='info',
                    msg=f'{message}\nОтсортированно за: {result_time} мс.')

# Окно программы
windows = Tk()
windows.title('Сортировка')
windows.geometry('360x180')

# Фрейм 1 - лейбл и окно ввода
frame_one = Frame(windows)
lbl_input = Label(frame_one, text='Введите последовательность чисел через запятую:')
lbl_input.pack(side='top', pady = 10)
entry_input = Entry(frame_one, width=50)
entry_input.pack(side='left')

# Фрейм 2 - лейб и список сортировок
frame_two = Frame(windows)
lbl_list = Label(frame_two, text='Выберите вариант сортировки:')
lbl_list.pack(side='left', pady = 20)
cobmo_list = ttk.Combobox(frame_two, values=list(SORT_TYPES))
cobmo_list.pack(side='left', pady = 20)

# Кнопка ввода
btn = Button(windows, text='Сортировать', command=input_processing)

# Расположение в окне
frame_one.pack()
frame_two.pack()
btn.pack(pady = 10)
# frame_three.pack()

windows.mainloop()
