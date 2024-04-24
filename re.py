#autoNUM r"[A-Z]\d{3}[A-Z]{2}\d{2,3}RUS"
import re
n = input("Введите номер авто:")
p = re.compile(r'(\S{1}).*?(\S{3}).*?(\S{2}).*?(\S{2})')
if re.match(p,n):
    print("Штраф на номер: "+n+" отправлен!")
else:
    print("Не правильно идентифицирован номер автомобиля!")