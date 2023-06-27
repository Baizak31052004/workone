#1 код

d = {True: "yes", 1: "no", 1.0: "maybe"}
print(len(d))

# это  одинаковых объекта, у них один и тот же хеш и True == 1 == 1.0 -> True, поэтому в результате получим одно значение

# # 1. 1
# # 2. 2  *
# # 3. 3
# # 4. Ошибку
  


# #2 код 

x = [{1}] * 2
x[0].add(2)
print(x)

#[{1}] * 2 -> [{1}, {1}] Но вторая ссылка указывает на первый объект,поэтому все
#изменение в первом,повлияют на второй и новорот.

# # 1. [{1,2}, {1}]
# # 2. [{1,2}, {1,2}] *
# # 3. [{1}, {1}]
# # 4. Ошибка



# #3 код

# s = {1, 2, 3}
# print(s[1])

# Множество-неиндексируемая коллекция,а значит мы не можем получить значение по индексу ([1])

# # 1. 1
# # 2. 2
# # 3. Ошибку *
# # 4. 3




# #4 код

odd = lambda x: bool(x % 2)
numbers = [n for n in range(10)]
print(numbers)
n = list()
for i in numbers:
    if odd(i):
        continue
    else:
        break

# #Код возвращает новый список,содержащий целые числа до 10 (иключая 10)

# 1. [0, 2, 4, 6, 8, 10]
# # 2. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  *
# # 3. [1, 3, 5, 7, 9]
# # 4. Ошибка



# #5 код

def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q) 

# #Списки передаются по ссылке.

# # 1. [0]
# # 2. [1]  *
# # 3. [1,0]
# # 4. Ошибку



# #6 код

print([1, 2, 3] == sorted ([1, 2, 3]))
print((1, 2, 3) == sorted ((1, 2, 3)))

# #sorted вщзвращает отсортированный список элементов последовательности.Во втором случае список не равен кортежу.

# # 1. True, False  *
# # 2. False, True
# # 3. False, False
# # 4. True, True




# #7 код

def foo(fname, val):
    print(fname(val))
foo(max, [1, 2, 3])
foo(min, [1, 2, 3])

# # #Имена функций можно передовать в качества аргументов в другие функции.

# # 1. 3,1   *
# # 2. 1,3
# # 3. Ошибка
# # 4. Перечисленные варианты не подходят




# #8 код

a = ([],)
a[0].extend([1])
print(a[0] == [1])

# Сам кортеж представляет собой неизменямый объект, но список,как
# изменяемая последовательность,может быть расширен.

# # # 1. True  *
# # # 2. False
# # # 3. Error
# # # 4. Ошибка




# #9 код

class A:
    n = 0

    def __str__(self):
        return str(self.n + 9)
    
    def __repr__(self):
        return str(self.n - 9 / 9)
    
print({A(), A()})

# # # Объекты класса не могут сравниться друг с другом,поэтому они считаются разными объектами.

# # 1. {-1.0}
# # 2. {-1.0, -1.0}
# # 3. {-1.0,9}
# # 4. Будет Ошибка



# #10 код

x = ['ad', 'cd']
for i in x:
    i.upper()
print(x)

# # #Функция upper() не изменяет исходную строку,а возвращает новую,котороя здесь не было нигде сохранена.

# # 1. ['ad', 'cd']  *
# # 2. ['AB', 'CD']
# # 3. ['None', 'None']
# # 4. Ничто из перечисленного
