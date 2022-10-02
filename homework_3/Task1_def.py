#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

def lst():
    number = int (input('input a number '))
    ls=[]
    for i in range(number):
        ls.append (random.randint(1,10))
    return ls
#n=int(input('Enter a number '))
#ls=[]
#for i in range (n):
    #ls.append(random.randint(1,10))
#print(ls)
ls = lst()
print (ls)

def sum (lst):
    sum = 0
    for i in range (len(lst)):
        if i%2==0:
           sum+=lst[i]
    return sum


print (sum (ls))
