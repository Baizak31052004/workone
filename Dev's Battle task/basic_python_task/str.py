text = 'Задание с подвохом?'

a = text.capitalize()
b = text.title()

print(a[10] + b[10])

shiv = (11, 5, 7, 2, 2, 3)
shiv = str(shiv)

print(shiv[5])

company = "Dory-or"
counter = {}
for char in company:
    if char not in counter:
        counter[char] = 0
    counter[char] += 1
    
print(counter)

s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))

# print(ord('foo'))

a = iter("a")
print(a)

a = iter({1})
print(a)

text = 'ABS'
x = text.ljust(5, '*').rstrip('*').rjust(4, '*')
print(x)

c = 'd'
n = ord(c) - ord('a') + 1
print("Его номер", n)


