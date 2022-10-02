#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def fill_list(number):
    ls=sample(range(1,number*2),number)
    return ls

def multy(lst):
    lst1=[]
    len_lst=len(lst)//2
    for i in range(len_lst):
        lst1.append(lst[i]*lst[len(lst)-1-i])
    if len(lst)%2:
        lst1.append(lst[len(lst)//2])
    return lst1

start_list=fill_list(int(input('Enter a number ')))
print (start_list)
print (multy(start_list))