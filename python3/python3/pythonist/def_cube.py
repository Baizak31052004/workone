def cube(num):
    return num * num * num


print(cube(3))

# 2)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
    
print(max_num(3, 40, 5))