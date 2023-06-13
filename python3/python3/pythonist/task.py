from functools import partial, reduce


def power(x, exponent):
    return x ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)


print(square(4))
print(cube(4))


# 2)
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


# 3)
numbers_one =[1, 2, 3, 4, 5, 6]
even_numbers_one = list(filter(lambda x: x % 2 == 0, numbers_one))
print(even_numbers_one)

# 4)
def test():
    s = 0
    while True:
        x = yield s
        s += x
        

t = test()
next(t)
print(t.send(111))
print(t.send(123))
print(t.send(456))
print(t.send(789))
print(t.send(1000))

# 5)
a = [1,2,3,4,5]
for i in a:
 if i > 3:
  pass
 print(i)