#---------------------------
folder_path = '/Users/valeriie/Desktop/Python with V/lessons/'

file_name = folder_path + '33_txt.txt'

f = open(file_path + '22_txt', 'w')

f.write('Hello world\n')
f.write('Hello world\n')
f.write('Hello world\n')
f.write('Hello world\n')

f.close()



with open(file_name, 'w', encoding='utf-8') as f:
    f.write('Hi world')


#---------------------------
dl = ['Anna', 'Vadim', 'Natalia', 'Milana']

with open(file_name, 'w', encoding='utf-8') as f:

    for line in dl:
        f.write(line)
        f.write('\n')

#---------------------------проверять и записывать новый файл
file_name = folder_path + '44_txt.txt'
with open(file_name, 'x') as f:
    f.write('Hi World!')

#---------------------------
file_name = folder_path + '44_txt.txt'
with open(file_name, 'a') as f:
    f.write('Hi World!\n')

#---------------------------читать файлы
with open(file_name, 'r') as f:
    # ff = f.read()
    ff = f.read(11)
    ff = f.readlines()

    for i in ff:
        print(i)

    print(ff)

#---------------------------csv таблицы записаны в виде строк
import csv

csv_file_name = folder_path + '55_csv.csv'

dl = ['Anna', 'Vadim', 'Natalia', 'Milana']

with open(csv_file_name, 'w') as csv_f:
    writer = csv.writer(csv_f)
    row = ['Alex', 32]
    writer.writerow(row)

#---------------------------создания списка
users_list = [
    ['Vadim', 33],
    ['Alex', 32],
    ['Anna', 30]
]

with open(csv_file_name, 'a') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerows(users_list)

#---------------------------читать
with open(csv_file_name, 'r') as csv_f:
    reader = csv.reader(csv_f)

    for row in reader:
        print(row)

#---------------------------оглавление столбов
users = [
    {'name': 'Vadim', 'age': 32},
    {'name': 'Anna', 'age': 20},
    {'name': 'Alex', 'age': 25},
    {'name': 'Elena', 'age': 18},
]

with open(csv_file_name, 'w') as csv_f:
    columns = ['name', 'age']

    writer = csv.DictWriter(csv_f, fieldnames=columns)
    writer.writeheader()

    writer.writerows(users)

    user = {'name': 'Elena', 'age': 18}
    writer.writerow(user)


#---------------------------
with open(csv_file_name, 'r') as csv_f:
    reader = csv.DictReader(csv_f)

    for row in reader:
        print(row['name'], row['age'])
