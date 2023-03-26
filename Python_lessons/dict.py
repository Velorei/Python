#------------------------------------
dict_item = {}

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,5,6],
    3: {'name': 'Vadim', 'age': '32', 'salary': 10000}
}

print(1, ':', dict_item[1])
print(3, ':', dict_item[3]['name'])

x = dict_item.get(3).get('salary')
print(x)

dict_item['city'] = 'Lviv'
print(dict_item)

dict_item[1] = 'Georgy'
print(dict_item)

#------------------------------------удалить определенный элемент
del dict_item[2]

print(dict_item)

#------------------------------------удалить последний эдемент
dict_item.popitem()
print(dict_item)

#------------------------------------чистить весь дикт
dict_item.clear()
print(dict_item)

#------------------------------------сделать копию
dict_item = {}

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,5,6],
    3: {'name': 'Vadim', 'age': '32', 'salary': 10000}
}

print(dict_item)

dict_2 = dict_item
print('dict_2', dict_2)

dict_2['city'] = 'Dnepr'

dict_3 = dict_item.copy()
print('dict_3', dict_3)

dict_4 = dict_item.copy()
print('dict_4', dict_4)


#------------------------------------проитерировать
dict_item = {}

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,5,6],
    3: {'name': 'Vadim', 'age': '32', 'salary': 10000}
}

for key, value in dict_item.items():
    print('key:', key, 'value:', value)

#------------------------------------итариация
dict_item = {}

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,5,6],
    3: {'name': 'Vadim', 'age': '32', 'salary': 10000}
}

for key in dict_item:
    print('item:', dict_item[key])

#------------------------------------значение добавить каждому из item
names = ('Vadim', 'Inna', 'Dmitriy')
salary = 10000
dd = dict.fromkeys(names, salary)

print(dd)
#------------------------------------создание json file
import json

path = '/Users/valeriie/Desktop/Python with V/lessons/'
file_title = 'python_json_lesson.json'

full_name = path + file_title

dict_item = {
    1: 'Julia',
    2: [1,2,3,4,5,6],
    3: {'name': 'Vadim', 'age': '32', 'salary': 10000},
    'city': 'Dnepr',
    False: 'False',
    '[1,2,3]': 'Dmitriy'
}

with open(full_name, 'w') as jf:
    json.dump(dict_item, jf)

#------------------------------------прочитать
with open(full_name, 'r') as jf:
    json_data = jf.read()
    json_object = json.loads(json_data)

    print('json_data:', json_data, type(json_data))
    print('json_object:', json_object, type(json_object))
    print(json_object['city'])
