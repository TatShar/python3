#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
a=int(input('input a number '))
lst = []
for i in range(a):
    b=random.uniform(0,10)
    lst.append(round(b,1))
print(lst)
c=1
max = lst[0]
min = lst[0]
while c<=len(lst)-1:
    if (lst[c]*10)%10 > (max*10)%10:
        max=lst[c]
    elif (lst[c]*10)%10 < (min*10)%10:
        min=lst[c]
    c+=1 
print (max)
print (min)
print (round((max%1 - min%1),1))