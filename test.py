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