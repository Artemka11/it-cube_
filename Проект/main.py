import pygame as pg
pg.init ()
clock = pg. time. Clock()
FPS = 10
WINDOWSIZE =(700,700)
pg.display.set_mode (WINDOWSIZE)

run = True 
while run:
    for event in pg-event. get ():
        if event. type == pg-QUIT:
            pg.quit ()
run = False
clock.tick(FPS)



import numpy as np # подключаем библиотеку numpy
text = open('kargo.txt', encoding='utf8').read() # в переменную отправляем все содержимое файла
corpus = text.split() # разбиваем текст на отдельные слова
def make_pairs(corpus): # делаем новую функуию, определятель пар слов
    
    for i in range(len(corpus)-1):  # перебираем все слова в корпус, не включая последний
        yield (corpus[i], corpus[i+1]) # генерируем пару и задаем её как результат функции
pairs = make_pairs(corpus) # этим генератором получаем все пары слов
word_dict = {} # словарь на старте пуст

for word_1, word_2 in pairs: # перебираем все слова по два слова из готового списка парных слов
    if word_1 in word_dict.keys(): # если типа первое слово есть в словаре
         word_dict[word_1].append(word_2) #то добавляем второе слово как продолжение первого
    else: #иначе
        word_dict[word_1] = [word_2] # создаём запись в словаре и указываем второе слово как продолжение первого
        first_word = np.random.choice(corpus) # случайно выбирается первое слово для старта

while first_word.islower(): # пока в нашем первом слове нет больших букв
    first_word = np.random.choice(corpus) # то выбираем новое слово случайным образом
                                          # и так до тех пор, пока не найдём слово с большой буквой
    chain = [first_word] # делаем наше первое слово первым звеном
n_words = int(input("количество слов для проверки вашей скорости печати ЫЫ")) # сколько слов будет в готовом тексте

for i in range(n_words): # делаем цикл с нашим количеством слов
    chain.append(np.random.choice(word_dict[chain[-1]])) # на каждом шаге добавляем следующее слово из словаря, выбирая его случайным образом из доступных вариантов
print(' '.join(chain)) #результат выводится! текст готов