# """ 
# Арифметические операторы в Python
#         +   Добавление
#         -   Вычитание
#         *   Умножение
#         /   Деление - делит левый операнд на правый
#         %   Модуль - делит левый операнд на правый и возвращает остаток
#         **  Возведение в степень
#         //  Деление с остатком
# """

# """
# Операторы сравнение в Python
#     1)    ==  проверяет одиноково ли значение операндовы если одинаковы - то условие является истинной (True); (a == b)False
#     2)    !=  проверяет одиноково ли значение операндовы если НЕ одинаковы - то условие является истинной (True); (a != b) True
#     3)    <> проверяет одиноково ли значение операндовы если НЕ одинаковы - то условие является истинной (True); (a <> b) True
#     4)    > проверяет значение левого оператора если он больше чем правый - то условие является истинной; (a > b) False
#     5)    < проверяет значение левого оператора если он больше чем правый - то условие является истинной; (a < b) True
#     6)    >= проверяет значение левого оператора, если он больше или равен правому  - то условие является истинной; (a >= b) False
#     7)    <= проверяет значение левого оператора, если он больше или равен правому  - то условие является истинной; (a <= b) True
# """

# """ 
# Логические операторы в Python
#     and - AND (И). Если оба операнда = True выражение будет так же True;    (a and b) is True.
#     or - OR (ИЛИ). Если хотя бы из двух операторов не пустой (не равен 0) - выражения истинно; (a or b) is True.
#     not - NOT (НЕ)Ю Используется для обратного изменения логического результата выражения.       
# """

# """ 
# Операторы принадлежности в Python
#     in - Считается истинной (True), если находит переменную в заданной последовательностиб и ложьью (False) в противном случае; not in - Считается истинной (True), если не находит переменную в заданной последоввательности, и ложью (False) в противном случае
# """

# """ 
# Операторы тождественности в Python
#     is - Считается истинной (True), если переменные по обе стороны указывают на один объект, и ложью (False)
#     is not - Считается ложью (False), если оба переменные по себе стороны от оператора указывают на один объект, и истинной (True)
# """

# """ 
# Битовые операторы в Python
# & - AND
# ! - OR
# ^ - XOR
# ~
# <<
# >>
# """




# # s = 5 + 5
# # print(s)

# # c = 5
# # a = 5
# # if c > a:
# #     print("Больше")
# # else:
# #     print("Меньше или ровно")

# # a = 10
# # b = 6
# # d = a is b
# # print(d)




# c = 10
# a = 20
# list = [1,2,3,34,5,10]
# if (c in list):
#     print("True")
    
    
sum = 0
index = -20

for index in range(1, 11):
    sum = sum + index
    
    if index == 5:
        print('Это верно')
        continue
    
    print(sum)