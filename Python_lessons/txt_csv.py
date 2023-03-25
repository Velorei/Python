#-------------------------------
file_path = '/Users/valeriie/Desktop/Python with V/lessons/'
file_name = 'txt_lesson_7.txt'

file_path_name = file_path + file_name
print(file_path_name)

f = open(file_path_name, 'w')
f.write('Hello Ukraine!')

f.close()


#-------------------------------перезаписаь файл
with open(file_path_name, 'w') as txt_file:

    name = 'Vadim '
    surname = 'Popov\n'
    full_name = name + surname

    txt_file.write(full_name)

#-------------------------------добавить в файл
with open(file_path_name, 'a') as txt_file:

    name = 'Alexey '
    surname = 'Borisovish\n '
    full_name = name + surname

    txt_file.write(full_name)

#-------------------------------
# with open(file_path_name, 'a') as txt_file:
#
#     name = input('name: ')
#     surname = input('surname: ')
#     full_name = name + surname + '\n'
#
#     txt_file.write(full_name)

#-------------------------------список в новую строку
file_path_name = file_path + file_name
names_list = ['Julia', 'Lyana', 'Alina', 'Dmitriy']

with open(file_path_name, 'w') as txt_file:

    for i in names_list:

        txt_file.write(i)
        txt_file.write('\n')

#-------------------------------переход в новую строку
file_path_name = file_path + file_name
names_list = ['Julia', 'Lyana', 'Alina', 'Dmitriy']

with open(file_path_name, 'r') as txt_file:

    read_f = txt_file.readlines()

    for i in read_f:
        print(i)

#-------------------------------переход в новую строку + показать тип
file_path_name = file_path + file_name
names_list = ['Julia', 'Lyana', 'Alina', 'Dmitriy']

with open(file_path_name, 'r') as txt_file:

    read_f = txt_file.readlines()

    for i in read_f:
        print(i.rstrip(), type(i))

#-------------------------------
import csv

file_path = '/Users/valeriie/Desktop/Python with V/lessons/'
file_name = 'txt_lesson_7.csv'
csv_file_name = file_path + file_name

user_list = [
    ['Vadim', 32],
    ['Alexey', 34],
    ['Julia', 19]
]

with open(csv_file_name, 'w') as cf:
    writer = csv.writer(cf)

    writer.writerows(user_list)

#-------------------------------генерация данных
import csv

file_path = '/Users/valeriie/Desktop/Python with V/lessons/'
file_name = 'txt_lesson_7.csv'
csv_file_name = file_path + file_name

name_age = []


user_list = [
    ['Vadim', 32],
    ['Alexey', 34],
    ['Julia', 19]
]

new_user_list = []

for item in range(0, 100):

    for ul_item in user_list:
        name_age = []

        new_name = ul_item[0] + '_' + str(item)

        new_age = 10 + item
        name_age.append(new_name)
        name_age.append(new_age)

        new_user_list.append(name_age)

for ii in new_user_list:
    print(ii)

with open(csv_file_name, 'a') as cf:
    writer = csv.writer(cf)

    writer.writerows(new_user_list)
