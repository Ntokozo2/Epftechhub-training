num1 = 1
num2 = 2
sum = 0
next_value = 0


while sum <= 4000000:
    next_value = num1
    num1 = num2
    num2 = next_value + num2

    if next_value % 2 == 0:
        sum += next_value
     
print(sum)
