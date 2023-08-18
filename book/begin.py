Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
8 * 3,57
(24, 57)
8 * 3.57
28.56
10 * 365
3650
20 + 3650
3670
3 * 52
156
3670 - 156
3514
100 / 20
5.0
5 + 30 * 20
605
(5 + 30) * 20
700
(5 + 30) * 20) / 10
SyntaxError: unmatched ')'
((5 + 30) * 20) / 10
70.0
5 + 30 * 20 / 10
65.0
fred = 100
print (fred)
100
fred = 200
print (fred)
200
john = 300
print (john)
300
john = fred
print (john)
200
print (fred)
200
number_of_coins = 200
print (number_of_coins)
200
20 + 10 * 365
3670
3 * 52
156
>>> 3670 - 156
3514
>>> 20 + 10 * 365 - 3 * 52
3514
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> found_coins +magic_coins * 365 - stolen_coins * 52
3514
>>> 
>>> stolen_coins = 2
>>> found_coins +magic_coins * 365 - stolen_coins * 52
3566
>>> magic_coins = 13
>>> found_coins +magic_coins * 365 - stolen_coins * 52
4661
>>> fred = "Почему у горилл большие ноздри? Потому что у них толстые пальцы"
>>> print (fred)
Почему у горилл большие ноздри? Потому что у них толстые пальцы
>>> fred = 'Что это: розовое и пушистое? Розовый пушистик'
>>> print (fred)
Что это: розовое и пушистое? Розовый пушистик
>>> fred = '''Что едят на полдник динозавры?
... ТиРекс-кекс!'''
>>> print (fred)
Что едят на полдник динозавры?
ТиРекс-кекс!
>>> silly_string = '''"Тут что-то не так, не будь я д'Артаньян", - подумал он.'''
>>> print (silly_string)
"Тут что-то не так, не будь я д'Артаньян", - подумал он.
>>> single_quote_str = '"Тут что-то не так, не будь я д\'Артаньян", - подумал он.'
>>> print (single_quote_str)
"Тут что-то не так, не будь я д'Артаньян", - подумал он.
>>> double_quote_str = "\"Тут что-то не так, не будь я д'Артаньян\", - подумал он."
>>> print (double_quote_str)
"Тут что-то не так, не будь я д'Артаньян", - подумал он.
>>> myscore = 1000
>>> message = 'Мой счет: %s очков'
>>> print(message %s myscore)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print (message %s myscore)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(message % myscore)
Мой счет: 1000 очков
>>> print(message % 1000)
Мой счет: 1000 очков
>>> joke_text = '%s: приспособление для поиска мебели в темноте'
>>> bodypart1 = 'Коленка'
>>> bodypart2 = 'Лодыжка'
>>> print(joke_text % bodypart1)
Коленка: приспособление для поиска мебели в темноте
>>> print(joke_text % bodypart2)
Лодыжка: приспособление для поиска мебели в темноте
>>> nums = 'ЧТо сказало число %s числу %s? Славный поясок!'
>>> print(nums % (0, 8))
ЧТо сказало число 0 числу 8? Славный поясок!
>>> print (10 * 'a')
aaaaaaaaaa
