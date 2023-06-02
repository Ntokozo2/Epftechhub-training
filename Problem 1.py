endNum = 999
sum = 0
for i in range(0, endNum+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

