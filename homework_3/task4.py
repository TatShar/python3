#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
a = int (input('input a number '))
#print (bin(a))
b=''
while a > 0:
    b=str(a%2)+b
    a=a//2
print (b)


