num1 = 1
num2 = 2
sum = 0
next_value = 0


while sum <= 4000000:
    num2 = num1 + num1
    num  = num1
    num1 = num2
    

    if num2 % 2 == 0:
        sum += num2
     
print(sum)