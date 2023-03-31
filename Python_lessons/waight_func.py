import random

u_list = []
uu_list = []
d_list = []

for i in range(0, 20):
    dd = random.randint(0, 10)
    d_list.append(dd)

    if dd in u_list:
        continue
    else:
        sql_str = '(' + "'" + str(dd) + "'" + ')'

        u_list.append(dd)

print('d_list = ', d_list)
print('u_list = ', u_list)

print('insert into Person(person_name, city_id) values')

for ii in u_list:
    sql_str = '(' + "'" + 'Vadim_' + str(ii) + "'" + "," + str(ii) + ')'
    print(sql_str)
