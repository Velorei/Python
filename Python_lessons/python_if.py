item_1 = 1
item_0 = 0

name = 'Vadim'
name_e = ''

none_item = None

items_list = ['11', 22]
items_list_e = []


b_item_t = True
b_item_f = False

####-----------------------------
if item_1:
    print('True item')
else:
    print('False item')


####-----------------------------
if name_e:
    print('True item')
else:
    print('False item')


####-----------------------------
if none_item:
    print('True item')
else:
    print('False item')
####-----------------------------
if b_item_t:
    print('----- True item')


####-----------------------------
compare_item = item_1 > item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 < item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 == item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 >= item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 <= item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 > item_0

if compare_item:
    print('True item')
else:
    print('False item')


####-----------------------------
compare_item = item_1 > item_0

if compare_item:
    print('---1 True item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')


####-----------------------------
compare_item = item_1 > item_0

if compare_item:
    print('---1 True item')
    if b_item_t:
        print('inner IF --1 -- TRue item')


####-----------------------------
compare_item = item_1 > item_0

if compare_item:
    print('---1 True item')

    new_name = 'Natalia'
    user_age = 30

    if new_name:
        new_user_age = user_age - 5

        print('new_user_age', new_user_age)


####-----------------------------& (и)
if compare_item & b_item_t:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')


####-----------------------------and (и)
if compare_item & b_item_t:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')

####-----------------------------or (или)
if compare_item or b_item_t:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')


####-----------------------------and (и - все условия обязательны)
if compare_item and b_item_t and items_list:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')


####-----------------------------and or (и/  или)
if compare_item and b_item_t or items_list_e:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')

####-----------------------------not
b_item_t = True
b_item_f = False

item_1 = 122
item_0 = 122

compare_item = item_1 >= item_0

if not compare_item:
    print('---1 --- compare_item item')
elif name_e:
    print('---2 Name item')
elif items_list_e:
    print('---3 Items_list')
elif 10 > 20:
    print('---4 Items_list')
else:
    print('---5 False item')
