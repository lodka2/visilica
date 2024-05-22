import os
import random

# clear lambda: os.system('cls')
print('привет! Я загадал слово, твоя задача-угадать его по буквам.')
input('*Нажми enter,чтобы продолжить*')
# clear()
print('Поехали!')
words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

for symb in word:

    print(symb, end=' ')
letters = []
isWin = True
hp = 10
while hp > 0:
    isWin = True
    letter = input('введите букву: ')
    letters.append(letter)
    for symb in word:
        if symb in letters:
            print(symb,end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты угадал! Молодец!')
        break

    if letter not in word:
        hp -= 1
        print(f'осталось попыток{hp}')
if hp == 0:
    print('ты проиграл!')