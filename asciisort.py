# допустим у нас есть несортированный массив из печатных ASCII символов
list = ['a','e','s','d','f','g','q','o']
# конвертировать каждый элемент массива в DEC формат
new_l=[ord(i) for i in list]
# произвести сортировку
new_l.sort()
# конвертировать обратно в Char
list=[chr(x) for x in new_l]
print(list)
