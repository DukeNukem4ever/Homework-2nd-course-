import random

# ПАРАМЕТРЫ:

weapons = ' '.join(open('Оружие.txt', 'r', encoding='utf-8').readlines()).split()
transport = ' '.join(open('Транспорт.txt', 'r', encoding='utf-8').readlines()).split()
electronics = ' '.join(open('Электроприборы.txt', 'r', encoding='utf-8').readlines()).split()

def getRandomWord1(weapons):
    wordIndex = random.randint(0, len(weapons) - 1)
    return weapons[wordIndex].upper()

def getRandomWord2(transport):
    wordIndex = random.randint(0, len(transport) - 1)
    return transport[wordIndex].upper()

def getRandomWord3(electronics):
    wordIndex = random.randint(0, len(electronics) - 1)
    return electronics[wordIndex].upper()

standard = 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
attempts = 9
HANGMANPICS = ['''
     o---o
     |   |
         |
         |
         |
         |
  =========''','''
     o---o
     |   |
     O   |
         |
         |
         |
  =========''','''
     o---o
     |   |
     O   |
     |   |
         |
         |
  =========''','''
     o---o
     |   |
     O   |
    /|   |
         |
         |
  =========''','''
     o---o
     |   |
     O   |
    /|\  |
         |
         |
  =========''','''
     o---o
     |   |
     O   |
    /|\  |
    /    |
         |
  =========''','''
     o---o
     |   |
     O   |
    /|\  |
    / \  |
         |
  =========''','''
     o---o
     |   |
    [O   |
    /|\  |
    / \  |
         |
  =========''','''
     o---o
     |   |
    [O]  |
    /|\  |
    / \  |
         |
  =========''']

def displayBoard(HANGMANPICS, Missing, Pravilno, goal):
     print(HANGMANPICS[len(Missing)])
     print()

     print('Неправильные буквы:', end=' ')
     for letter in Missing:
         print(letter, end=' ')
     print()

     blanks = '_' * len(goal)
     for i in range(len(goal)):
         if goal[i] in Pravilno and goal[i] in standard:
             blanks = blanks[:i] + goal[i] + blanks[i+1:]
     for letter in blanks: 
         print(letter, end=' ')
     print()

def Attempt(alreadyGuessed):
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.upper()
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in standard:
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

# ОСНОВНАЯ ПРОГРАММА:
print("Добро пожаловать!")
print(" ")
print("Выберите тему:")
print("1 - Оружие")
print("2 - Виды транспорта")
print("3 - Электроприборы")
answer = input()
if answer == "1":
    Missing = ''
    Pravilno = ''
    goal = getRandomWord1(weapons)
    gameIsDone = False
    print("У вас ДЕВЯТЬ попыток, чтобы отгадать слово из " + str(len(goal)) + " букв!")
    while True:
        displayBoard(HANGMANPICS, Missing, Pravilno, goal)
        guess = Attempt(Missing + Pravilno)
        if guess in goal:
            Pravilno = Pravilno + guess

            foundAllLetters = True
            for i in range(len(goal)):
                if goal[i] not in Pravilno:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('ПОБЕДА! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break
        else:
            Missing = Missing + guess
            attempts -= 1
            if attempts == 8:
                print("!!!!!ОСТАЛОСЬ ВОСЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 7:
                print("!!!!!ОСТАЛОСЬ СЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 6:
                print("!!!!!ОСТАЛОСЬ ШЕСТЬ ПОПЫТОК!!!!!")
            elif attempts == 5:
                print("!!!!!ОСТАЛОСЬ ПЯТЬ ПОПЫТОК!!!!!")
            elif attempts == 4:
                print("!!!!!ОСТАЛОСЬ ЧЕТЫРЕ ПОПЫТКИ!!!!!")
            elif attempts == 3:
                print("!!!!!ОСТАЛОСЬ ТРИ ПОПЫТКИ!!!!!")
            elif attempts == 2:
                print("!!!!!ОСТАЛОСЬ ДВЕ ПОПЫТКИ!!!!!")
            elif attempts == 1:
                print("!!!!!ОСТАЛАСЬ ОДНА ПОПЫТКА!!!!!")
            
            if len(Missing) == len(HANGMANPICS):
                print('''
     o---o
     |   |
    [X]  |
    /|\  |
    / \  |
         |
  =========
  GAME OVER!''')
                print(" ")
                print('ПОРАЖЕНИЕ! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break
elif answer == "2":
    Missing = ''
    Pravilno = ''
    goal = getRandomWord2(transport)
    gameIsDone = False
    print("У вас ДЕВЯТЬ попыток, чтобы отгадать слово из " + str(len(goal)) + " букв")
    while True:
        displayBoard(HANGMANPICS, Missing, Pravilno, goal)
        guess = Attempt(Missing + Pravilno)
        if guess in goal:
            Pravilno = Pravilno + guess

            foundAllLetters = True
            for i in range(len(goal)):
                if goal[i] not in Pravilno:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('ПОБЕДА! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break
        else:
            Missing = Missing + guess
            attempts -= 1
            if attempts == 8:
                print("!!!!!ОСТАЛОСЬ ВОСЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 7:
                print("!!!!!ОСТАЛОСЬ СЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 6:
                print("!!!!!ОСТАЛОСЬ ШЕСТЬ ПОПЫТОК!!!!!")
            elif attempts == 5:
                print("!!!!!ОСТАЛОСЬ ПЯТЬ ПОПЫТОК!!!!!")
            elif attempts == 4:
                print("!!!!!ОСТАЛОСЬ ЧЕТЫРЕ ПОПЫТКИ!!!!!")
            elif attempts == 3:
                print("!!!!!ОСТАЛОСЬ ТРИ ПОПЫТКИ!!!!!")
            elif attempts == 2:
                print("!!!!!ОСТАЛОСЬ ДВЕ ПОПЫТКИ!!!!!")
            elif attempts == 1:
                print("!!!!!ОСТАЛАСЬ ОДНА ПОПЫТКА!!!!!")
            
            if len(Missing) == len(HANGMANPICS):
                print('''
     o---o
     |   |
    [X]  |
    /|\  |
    / \  |
         |
  =========
  GAME OVER!''')
                print(" ")
                print('ПОРАЖЕНИЕ! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break

elif answer == "3":
    Missing = ''
    Pravilno = ''
    goal = getRandomWord3(electronics)
    gameIsDone = False
    print("У вас ДЕВЯТЬ попыток, чтобы отгадать слово из " + str(len(goal)) + " букв")
    while True:
        displayBoard(HANGMANPICS, Missing, Pravilno, goal)
        guess = Attempt(Missing + Pravilno)
        if guess in goal:
            Pravilno = Pravilno + guess

            foundAllLetters = True
            for i in range(len(goal)):
                if goal[i] not in Pravilno:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('ПОБЕДА! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break
        else:
            Missing = Missing + guess
            attempts -= 1
            if attempts == 8:
                print("!!!!!ОСТАЛОСЬ ВОСЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 7:
                print("!!!!!ОСТАЛОСЬ СЕМЬ ПОПЫТОК!!!!!")
            elif attempts == 6:
                print("!!!!!ОСТАЛОСЬ ШЕСТЬ ПОПЫТОК!!!!!")
            elif attempts == 5:
                print("!!!!!ОСТАЛОСЬ ПЯТЬ ПОПЫТОК!!!!!")
            elif attempts == 4:
                print("!!!!!ОСТАЛОСЬ ЧЕТЫРЕ ПОПЫТКИ!!!!!")
            elif attempts == 3:
                print("!!!!!ОСТАЛОСЬ ТРИ ПОПЫТКИ!!!!!")
            elif attempts == 2:
                print("!!!!!ОСТАЛОСЬ ДВЕ ПОПЫТКИ!!!!!")
            elif attempts == 1:
                print("!!!!!ОСТАЛАСЬ ОДНА ПОПЫТКА!!!!!")
            
            if len(Missing) == len(HANGMANPICS):
                print('''
     o---o
     |   |
    [X]  |
    /|\  |
    / \  |
         |
  =========
  GAME OVER!''')
                print(" ")
                print('ПОРАЖЕНИЕ! ЗАГАДАННОЕ СЛОВО: ' + goal)
                gameIsDone = True
                break
else:
    print("Пожалуйста, перезапустите программу и введите вариант ответа.")
    
