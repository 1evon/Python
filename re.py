#autoNUM r"[A-Z]\d{3}[A-Z]{2}\d{2,3}RUS"
import re
n = input("Введите номер авто в формате ""(Х000ХХ000)"":")
p = re.compile (r'(\w{1}).*?(\d{3}).*?(\w{2}).*?\d{2,3}') # r'[А-Я]\d{3}[А-Я]{2}\d{2,3}') r'[А-Я]\d{3}[А-Я]{2}\d{2,3}'
if re.match(p,n):
    print("Штраф на номер: "+n+" отправлен!")
else:
    print("Не правильно идентифицирован номер автомобиля!")