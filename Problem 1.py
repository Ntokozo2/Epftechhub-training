endNum = 999
sum = 0
 
while endNum > 0:
   num1 = endNum % 3
   num2 = endNum % 5
   if num1 == 0 or num2 == 0:
     sum += endNum
   endNum -= 1
   print(sum)


