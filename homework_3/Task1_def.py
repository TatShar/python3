#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sum ():
    lst =[1,2,3,4,5,6,]
    sum = 0
    for i in range (len(lst)):
        if i%2!=0:
            sum+=lst[i]
    return sum
print (sum ())
