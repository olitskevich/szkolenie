list = [1, 2, 3, 4]
sum = 0
sum1 = 0
sum2 = 1

for number in list:
    sum = number + sum
    #sum +=number
avr = sum/len(list)
print(avr)

for number in list:
    sum1 = number**2 + sum1
avr1 = sum1/len(list)
print(avr1)

for number in list:
    sum2 = number * sum2
    #sum2 *= number
avr2 = sum2** (1/len(list))
print(avr2)