a = 5
n = 0

# while a < 10:
    # print(a) будет писаться бесконечное кол. раз
    # print(n, ' == ', a)
    # n+=1 #сколько раз цикл успевается написаться


#бесконечный цикл
# while True:
#     print(n, ' == ', a)
#     n += 1

#--------------------------
while a <= 10:
    print(n, ' == ', a)
    a += 1
else:
    print(f'---- a == {a}')
    print('a == ', a)

#--------------------------что бы написать в столбик
message = 'good morning'

for m in message:
    print(m)

#--------------------------запись пошагово
message = 'good morning'

for m in range(0, 10):
    print(m)
#--------------------------запись через 2 шага
message = 'good morning'

for m in range(0, 10, 2):
    print(m)
#--------------------------в конце написать 'End'
message = 'good morning'

for m in range(0, 10, 2):
    print(m)
else:
    print('End')

#--------------------------вывести таблицу умножения
i = 1
n = 1

while i < 10:
    while n < 10:

        result = i * n

        print(result, end="\t")

        n +=1

    i += 1
    n = 1
    print("\n")

#--------------------------
n = 0

while n < 5:
    n += 1
    print('n --', n)

    if n == 3:
        print('n == ', 3)
        break

#--------------------------
message = 'good morning'
n = 0

while n < 5:
    n += 1
    print('n --', n)

    if n == 3:
        print('n == ', 3)
        continue

    print('Item n ==', n)

#--------------------------итерация массива
li = [1,4,7,9,2,3,56,87, 'ee', 'good', False, [33,66], {'key_1': 'value_1'}]

for i in li:

    if i == 'good':
        print('good in list')
        break

    print(i)
#--------------------------поиск в массиве
li = [1,4,7,9,2,3,56,87, 'ee', 'good', False, [33,66], {'key_1': 'value_1'}]
print('good' in li)

#--------------------------поиск в массиве
li = [1,4,7,9,2,3,56,87, 'ee', 'good', False, [33,66], {'key_1': 'value_1'}]

if 'good' in li:
    print(True)

#--------------------------проверка на тип
ll = [1,4,7,9,2,3,56,87, 'ee', 'good', False, [33,66], {'key_1': 'value_1'}]
for i in ll:
    if type(i) == list:
        for nn in i:
            print(nn)
