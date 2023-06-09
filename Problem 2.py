num1 = 0
num2 = 1
next_value = 1
sum = 0
dfsruthydur


while sum <= 4000000:
    next_value = num1
    num1 = num2
    num2 = next_value + num2

    if next_value % 2 == 0:
        sum += next_value
     
print(sum)
