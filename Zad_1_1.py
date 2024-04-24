#1
a = int(input("Введите 1 целое число:"))
b = int(input("Введите 2 целое число:"))
c = int(input("Введите 3 целое число:"))
s = max(a,b,c)
print(s)

#2
a = input("Введите 5 чисел через пробел:").split()
s = max(a)
print(s)

#3
a = int(input("Введите возраст Антона:"))
b = int(input("Введите возраст Бориса:"))
c = int(input("Введите возраст Виктора:"))
na ='Антон'
nb ='Борис'
nc ='Виктор'
okon='a'
s = max(a,b,c)
print ("Возраст",na+okon,":",a)
print("Возраст",nb+okon,":",b)
print("Возраст",nc+okon,":",c)

if a>b:
    if a>c: print (na+" старше всех")
    elif a!=b: print (na+" и",nb, " старше всех") 
    elif a!=c: print (na+" и",nc, " старше всех") 
elif b>a: 
    if b>c: print (nb+" старше всех")
    elif c!=b: print (nc+" и",nb," старше всех")
else: print (nc+" старше всех")  
