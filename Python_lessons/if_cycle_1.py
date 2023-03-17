b_item_t = True
b_item_f = False

item_1 = 122
item_0 = 122

compare_item = item_1 >= item_0
print(10 % 4)
##--в одну строчку код, который наполнил наш список элементами остаток от деления на 2 которых равен 0, тоесть четными числами
list_items = [result for result in range(0, 100) if result % 2]

for li in list_items:
    print('% result = ', li)

##--в несколько строк код, который наполнил наш список элементами остаток от деления на 2 которых равен 0, тоесть четными числами
list_items_1 = []
for result in range(0, 100):
    result_odd = result % 2
    if result_odd == 0:
        list_items_1.append(result)
