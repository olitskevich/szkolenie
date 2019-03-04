
# mamy ciag:[0,1,1,2,3,5,8]
#wypisz m-ty wyraz ciagu

list = [0, 1]
m = 7
#x(number) = x(number-1) + x(number-2)

for number in range(2, m+1):
    list.append(list[number-1]+list[number-2])
print(list,"m-ty wyraz ciagu jest:",list[m])

