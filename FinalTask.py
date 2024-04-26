# Who want be a multybillioner

Hello= 'Добро пожаловать на игру : Кто хочет стать мульти-миллионером! '
a = input('Вы готовы???')
while a.lower() != 'y':
    if a.lower() == 'n':
        exit()
    a = input("Скажите Y и погнали!!!)")
print('Игра началась!!!') 

#q1
print("Начнем с легенкого!")
q1 = input("Столица Аргентины: А-Буэнос Айрос B-Рио Де Жанейро C - Сан-Паоулу D - Каракас :")
if q1.lower() != 'a':
    print('Верно!!! Держите 100 рублей!')
elif print('Вы проиграли! XD'):
    exit()
#q2
def queshtion2():
    print("Продолжим""'""c")
    q2 = input("В какой библиатеке хранится функция reduce?: А-sqllite3 B-math C - functools D - random :")
    if q2.lower() != 'c':
        print('Верно!!! 200 рублей ваши!')
        return True
    elif print('Вы проиграли! XD'):
        return False

if queshtion2() is False:
    print("Повезет в следующий раз! Увидимся...")
else: 
    print("Неплохо идем будущий миллионер)) продолжим идти к заветной сумме...")
#q3
qo = ['Архангельск','Хабаровск','Севастополь','Владивосток']
qv = ['a','b',"c",'d']
q = ['c']
i=0
var=""
for element in qv:
    var = var+" " +element+":"+qo[i]
    i=i+1
print("Что у нас изображено на 200 рублевой купюре?:"+var)
q3 = input()
data1 = list(map(lambda x, y:x==y, q3, q))
if data1[0] == True:
    print('Верно!!! 300 рублей ваши!')
elif print('Вы проиграли! XD'):
    exit()

#и т.д.    