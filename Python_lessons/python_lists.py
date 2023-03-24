numbers_list = [1, 2, 3, 4, 5, 6, 7, 66, 22]
yololchka_list = list()  #пустой список

print(yololchka_list)

#----------------------------
yololchka_list_2 = [44,5,6,7]

yololchka_list_3 = numbers_list + yololchka_list_2

print(yololchka_list_3)

#----------------------------забрать какой то элемент со списка
numbers_list = [1, 2, 3, 4, 5, 6, 7, 66, 22, [11,22], [44,44]]

list_item = numbers_list[0]

print(list_item)

#----------------------------можно достать элемент в обратном порядке
numbers_list = [1, 2, 3, 4, 5, 6, 7, 66, 22, [11,22], [44,44]]

list_item = numbers_list[-2][-1]

print(list_item)

#----------------------------сгенерировать список одинаковых элементов
numbers_list = [7] * 6

print(numbers_list)

#----------------------------сгенерировать список до (числа)
numbers_list = list(range(30))

print(numbers_list)

#----------------------------сгенерировать список от (числа до числа)
numbers_list = list(range(10,30))

print(numbers_list)

#----------------------------сгенерировать список от (числа, до числа, и с добавлением шага)
numbers_list = list(range(10,30, 5))

print(numbers_list)

#----------------------------сгенерировать список в обратном порядке
numbers_list = list(range(30, 10, -1))

print(numbers_list)

#----------------------------
numbers_list = list(range(30, 10, -1))

multy_list = [1, True, 123, 13.5, 'Vadim', '123', [22,33], {1:'1'}, (1,5,6)]

print(multy_list)

#----------------------------проитерировать список
numbers_list = list(range(10))

multy_list = [1, True, 123, 13.5, 'Vadim', '123', [22,33], {1:'1'}, (1,5,6)]

for julia in numbers_list:
    print('Julia = ', julia)

for natalia in multy_list:
    print('Natalia = ', natalia, type(natalia))
    print('Natalia_item = ', multy_list[3], type(natalia))

#----------------------------проитерировать список
numbers_list = list(range(10))

multy_list = [1, True, 123, 13.5, 'Vadim', '123', [22,33], {1:'1'}, (1,5,6)]

print(multy_list)
print('len(multy_list) = ', len(multy_list))

for julia in range(0, len(multy_list)):

    list_item = multy_list[julia]

    print('Julia = ', multy_list[julia], type(multy_list))

#----------------------------итерировать списки
item = 0
while item < len(multy_list):

    list_item = multy_list[julia]

    print('Julia = ', multy_list[julia], type(multy_list))

    item += 1

#----------------------------
numbers_list = list(range(5))
numbers_list_2 = [0,1,2,3,4,5]

print('numbers_list = ', numbers_list)
print('numbers_list_2 = ', numbers_list_2)

if numbers_list == numbers_list_2:
    print('numbers_list == numbers_list_2', numbers_list == numbers_list_2)
else:
    print('numbers_list NOT numbers_list_2', numbers_list == numbers_list_2)

#----------------------------
numbers_list = list(range(5))
numbers_list_2 = [0,1,2,3,4]

print('numbers_list = ', numbers_list)
print('numbers_list_2 = ', numbers_list_2)

if numbers_list == numbers_list_2:
    print('numbers_list == numbers_list_2', numbers_list == numbers_list_2)
else:
    print('numbers_list NOT numbers_list_2', numbers_list == numbers_list_2)

#----------------------------добавить элемент в конец списка
names = ['Vadim', 'Alexey']

print('names =', names)

names.append('Julia')

print('names+ =', names)

#----------------------------добавить элемент на какую то конкретную позицию в списке
names = ['Vadim', 'Alexey', 'Julia']

names.insert(1, 'Inna')

print('names+ =', names)

#----------------------------достать  индекс определенного элемента со списка
names = ['Vadim', 'Inna', 'Alexey', 'Julia']

alex_index = names.index('Alexey')

print('names+ =', names)
print(alex_index)

#----------------------------добавить список в список
names = ['Vadim', 'Inna', 'Alexey', 'Julia']

add_items = ['Elena', 'Mikhail']
names.append(add_items)

print('names+ =', names)

#----------------------------добавить список в список но как элементы
names = ['Vadim', 'Inna', 'Alexey', 'Julia']

add_items = ['Elena', 'Mikhail']
names = names + add_items

print('names+ =', names)

#----------------------------удалить определенный элемент со списка по номеру
names = ['Vadim', 'Inna', 'Alexey', 'Julia']

names.pop(2)

print('names- =', names)

#----------------------------удалить определенный элемент со списка по имени
names = ['Vadim', 'Inna', 'Inna', 'Alexey', 'Julia']

names.remove('Inna')

print('names- =', names)

#----------------------------удалить определенный элемент со списка по имени даже если дублируется
names = ['Vadim', 'Inna', 'Inna', 'Alexey', 'Julia']

names.remove('Inna')

for item_name in names:
    if item_name == 'Inna':
        names.remove('Inna')


print('names- =', names)

#----------------------------
import random
names = ['Vadim', 'Inna', 'Inna', 'Alexey', 'Julia']
digits = []

rand = random.randint(0, 10)

for i in range(rand):

    d_int = random.randint(0, 10)
    digits.append(d_int)
    print('d_int', d_int)

print('digits_NOT_SORTED', digits)

digits.sort()

print('digits_SORTED', digits)

#----------------------------отсортировать список
names = ['Vadim', 'Inna', 'Inna', 'Alexey', 'Julia']

print('digits_NOT_SORTED', names)
names.sort()

print('digits_SORTED', names)

#----------------------------показать самое минимальное число
digits = [1,5,4,2,77,5,4,8,9,53,63,245676,43,764,785,0]

print('digits = ', digits)

min_digit = min(digits)
max_digit = max(digits)

print('min_digit = ', min_digit)
print('max_digit = ', max_digit)
