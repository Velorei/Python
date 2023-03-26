import csv

file_path = '/Users/valeriie/Desktop/Python with V/lessons/'
file_name = 'csv_lesson_8.csv'
csv_file_name = file_path + file_name

users_list = [
    ['Vadim', 33],
    ['Alex', 32],
    ['Anna', 30]
]

new_users_list = []

with open(csv_file_name, 'w') as cf:
    writer = csv.writer(cf)

    writer.writerows(users_list)

#----------------------------------добавление одной строчки в файлик
with open(csv_file_name, 'a') as csv_f:
    writer = csv.writer(csv_f)

    row_1 = ['Vlas', 25]

    writer.writerow(row_1)

#----------------------------------прописать хэдер
file_name = 'csv_lesson_8_headers.csv'
csv_file_name = file_path + file_name

users_list = [
    ['Vadim', 33],
    ['Alex', 32],
    ['Anna', 30]
]
users_dict = [
    {'name': 'Vadim', 'age': 32},
    {'name': 'Roman', 'age': 25},
    {'name': 'Vale', 'age': 25},
    {'name': 'Alexey', 'age': 19},
]

new_users_list = []

 with open(csv_file_name, 'w') as cf:
     columns = ['name', 'age']
     writer = csv.DictWriter(cf, fieldnames=columns)
     writer.writeheader()

#----------------------------------добавить строки под хэдер
     row_1 = {'name': 'Vlas', 'age': 25}
     writer.writerow(row_1)

#----------------------------------
with open(csv_file_name, 'a') as csv_f:
    columns = ['name', 'age']
    writer = csv.DictWriter(csv_f, fieldnames=columns)

    writer.writerows(users_dict)

#----------------------------------читать
with open(csv_file_name, 'r') as csv_f:

    reader = csv.DictReader(csv_f)
    line_count = 0

    age_list = []

    for row in reader:
        print(row['name'], row['age'])

#----------------------------------забрать возроста и вывести
        age_list.append(row['age'])

    print(age_list)
