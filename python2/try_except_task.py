# Обработайте исключение, которое вызывает код ниже, с помощью блоков try и except
for i in ['a', 'b', 'c']:
    print(i**2)
    
# задача 2)
# Обработайте исключение которое вызывает код ниже с помощью блоков try и except. затем изпользуйте блок finally, чтобы сказать что все сделано. 
x = 5
y = 0
z = x/y

# задача 3)
# Напишите функцию которое спрашивает пользователя ввести число, и затем выводит это число квадрате. Изпользуйте цикл while и блоки try, except и else для обработки некорректно введенных данных.

# def ask():
#     pass

# ask()

# terminal:
#     Введите число: null
#     Произошло ошибка! Попробуйте снова!
#     Введите число: 2
#     Квадрат число: 4



# 1)
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print('Произошло ошибка')
    

# 2)

try:
    x = 5
    y = 0
    z = x/y
except:
    print('ошибка')
finally:
    print('Все сделано!')
    
    
# 3)

def ask():
    while True:
        try:
            n = int(input('Введите число: '))
        except:
            print('Пожалуйста попробуйте снова! \n ')
            continue
        else:
            break
    print('квадрат число: ')
    print(n ** 2)
    
ask()