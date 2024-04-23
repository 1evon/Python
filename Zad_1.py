#1
a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
c = int(input("Введите число c:"))
s = a+b+c
u = a*b*c
sa = (a+b+c)/3
print ("Сумма чисел:",s, "Произведение чисел:",u, "Среднее арифметическое:",sa )

#3
from random import randint
x= randint(100,999)
x1 = x//100 
x2 = (x//10)%10 
x3 = x%10 
print(x1,x2,x3)

#2
import math
x = float(input("Введите x координату А:"))
y= float(input("Введите y координату А:"))
x2 = float(input("Введите x координату В:"))
y2 = float(input("Введите y координату В:"))
#формула?
length = math.sqrt((x2-x)**2+(y2-y)**2)
print(length)

