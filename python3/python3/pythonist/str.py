from re import search



# 1)
my_list = ["Pythonist.ru", "-", "хороший", "сайт", "по","Python"]
print(" ".join(my_list))

# 2)
my_list2 = [66, 77, 88, 99]
print(" ".join(map(str, my_list2)))

# 3)
my_list3 = [11, 22, 33, 44, 55]
print(str(my_list3).strip('[]'))

# 4)
def split(s):
    return [char for char in s]

s = 'Hdfs Tutorial'
print(s)
d = split(s)
print(d)
a = list(s)
print(a)

# 5)
children_boy_group1 = 'Nyrel'
children_boy_group2 = 'Nyrel223'

if children_boy_group1 in children_boy_group2:
    print('Он есть в группе')
else:
    print('Его нету')
    
# 6)
fullstring = "Deepl"
substring = "Deepl2"
try:
    fullstring.index(substring)
except ValueError:
    print("Подстрока не найдена!")
else:
    print("Подстрока найдена!")
    
# 7)
fullstring = "pythonist"
substring = "python"
if search(substring, fullstring):
    print("Подстрока найдена!")
else:
    print("Подстрока не найдена!")
    
# 8)
programming = "Javascript"
programming2 = "Java"
if fullstring.find(substring) != -1:
    print("Язык программирование есть")
else:
    print("Язык программирование нету")
    
# 9)
def urlify(s):
    s = s.strip().split(" ")
    return ("%20").join(s)


print(urlify("Dev's Battle "))

# 10)
str = "development"
stringlength = len(str) 
slicedString = str[stringlength::-1]  
print(slicedString)

# 11)
str = "programming" # исходная строка
reversedString=[]
index = len(str) # вычисляем длину строки и сохраняем ее в переменной index
while index > 0: 
    reversedString += str[ index - 1 ] # сохраняем значение str[index-1] в reverseString
    index = index - 1 # уменьшаем значение index на 1
print(reversedString) # перевернутая строка

# 12)
str = 'python' 
reversed=''.join(reversed(str))
print(reversed)