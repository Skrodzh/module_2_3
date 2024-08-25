my_list = [42, 69, 332, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0 # переменная счетчик
while a < len(my_list): # цикл должен работать до тех пор пока а < длины списка
    element = my_list[a]  # обращаемся к элементу по индексу - первый элемент цикла
    a = a + 1  # второй елемент цикла
    if element < 0:
        break
    elif element == 0:
        continue
    else:
        print(element)