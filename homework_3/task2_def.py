#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def mult():
    lst = [2,3,5,6]
    lst1=[]
    y=0
    z=len(lst)-1
    for i in range (len(lst)):
        if len(lst)%2!=0:
            if i<= round (len(lst)/2):
                lst1.append(lst[y]*lst[z])
                y+=1
                z-=1
            else: break
        else:
            if i< round (len(lst)/2):
                lst1.append(lst[y]*lst[z])
                y+=1
                z-=1
    return lst1
print(mult())