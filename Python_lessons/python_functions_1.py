def yolochka(a1, a2, a3):
    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3

    return var_1

get_f1 = yolochka(2, 5, 10)
print('get_f1 = ', get_f1)

#------------------------
def yolochka(a1, a2, a3):
    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3

    return var_1, var_2, var_3

get_f1, get_f11, get_f111 = yolochka(2, 5, 10)
print('get_f1 = ', get_f1)
print('get_f11 = ', get_f11)
print('get_f111 = ', get_f111)

#------------------------
def yolochka(a1, a2, a3):
    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3

    result = [var_1, var_2, var_3]

    return result

get_f1 = yolochka(2, 5, 10)
print('get_f1 = ', get_f1)

#------------------------
def yolochka(a1, a2, a3, a4=100, a5=200, a6='Vadim'): #именнованые параметры нужно писать после порядковых!!!
    var_1 = a1 * 2
    var_2 = a2 * 10
    var_3 = a3 * 3

    result = [var_1, var_2, var_3, a5]

    return result

get_f1 = yolochka(2, 5, 10, a5=500)
print('get_f1 = ', get_f1)

#-----------------------
def yolochka(*args):
    print(args)

get_f1 = yolochka(2, 5, 10)

#------------------------
def yolochka(*args):
    print(args)

a1, a2, a3 = 1, 2, 3

yolochka(a1, a2, a3)

#------------------------
def yolochka(**kwargs):
    print(kwargs)

yolochka(a1=1, a2=2, a3=3)

#------------------------
def yolochka(*args, **kwargs):
    print(args, kwargs)


yolochka(11, 22, 'Vadim', a1=1, a2=2, a3=3) #полный тюпл

#------------------------
def yolochka(salary, *args, **kwargs):
    print(salary, args, kwargs)


yolochka(1000, 11, 22, 'Vadim', a1=1, a2=2, a3=3)

#------------------------
def yolochka(salary, *args, **kwargs):

    for k, v in kwargs.items():

        n1 = v * 2
        print('K=', k, 'V=', n1)

    print(salary, args, kwargs)


yolochka(1000, a1=5, a2=10)

#------------------------
def yolochka(salary, *args, **kwargs):

    print(kwargs['a2'])

    for k, v in kwargs.items():

        n1 = v * 2
        print('K=', k, 'V=', n1)

    print(salary, args, kwargs)


yolochka(1000, a1=5, a2=10)
