
fio = input("Введите ФИО:")
r = fio.split()
f = r[0]
i = r[1]
o = r[2]
ii = i[:1]
oo = o[:1]
print(ii+'.',oo+".",f)

#replace
#(X > 0) and (Y < X) and (Z > Y) and (Z <> 5)
stroka = input("Введите :")
sim = stroka.find('and')
ns = stroka.replace("and","&")
print(ns)