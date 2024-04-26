words = ['4', '8', '15', 'восемнадцать']
max_word = ''#создаем пустую строку для хранения самого длинного слова
for word in words: #перебираем строки в списке
    if len(word) > len(max_word): #если длина текущей строки больше 
        max_word = word #обновляем значение переменной
print(max_word) #выводим итоговое значение на экран

numbs = ['4', '23', '15', 'sex']
int_numbs = map(int, numbs)
print(int_numbs) 

n =  [1,5,8,4,2]
n2 = [2,1,0,2,1]
funk = lambda x,y:x*y
a = list(map(funk,n,n2))
print(a)

words = ['шалаш', 'кот', 'топот', 'бег', 'анна']
pal_words = list(filter(lambda word: word == word[::-1], words))
print(pal_words)