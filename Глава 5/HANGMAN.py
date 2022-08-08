#Игра "Виселица", компьтер загадывает слово, а человек должен по буквам его отгадать

import random

HANGMAN = (
    """
    ------------
    |          |
    |          
    |        
    |        
    |         
    |         
    |       
    |
    """,
    """
    ------------
    |          |
    |          O
    |        
    |      
    |       
    |         
    |        
    |
    """,
    """
    ------------
    |          |
    |          O
    |        --+--
    |      
    |       
    |         
    |        
    |
    """,
    """
    ------------
    |          |
    |          O
    |       /--+--/
    |         
    |         
    |        
    |       
    |
    """,
    """
    ------------
    |          |
    |          O
    |       /--+--/
    |          |
    |          
    |         
    |        
    |
    """,
    """
    ------------
    |          |
    |          O
    |       /--+--/
    |          |
    |          |
    |         
    |        
    |
    """,
    """
    ------------
    |          |
    |          O
    |       /--+--/
    |          |
    |          |
    |        |    
    |        |   
    |
    """,
    """
    ------------
    |          |
    |          O
    |       /--+--/
    |          |
    |          |
    |        |   | 
    |        |   |
    |
    """
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("МАШИНА", "ЧЕЛОВЕК", "КОМПЬЮТЕР", "ТЕРМИНАТОР", "ИСКУССТВО", "ЗАДАЧА", "ПОДСТАКАННИК")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []
print('Добро пожаловать в игру "Виселица". Удачи вам!\n')
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\nВы уже предалагали следующие буквы:\n', used)
    print('\nОтгаданное вами в слове сейчас выглядит так:\n', so_far)
    guess = input('\n\nВведите букву: ')
    guess = guess.upper()
    while guess in used:
        print('Вы уже предлагали букву', guess)
        guess = input('\n\nВведите букву: ')
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print('\nДа! Буква', guess, 'есть в слове!')
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\n К сожалению, буквы', guess, 'нет в слове.')
        wrong += 1
        if wrong == MAX_WRONG:
            print(HANGMAN[wrong])
            print('\nВас повесили(((')
        else:
            print('\nВы отгадали!!!')
print('\nБыло загадно слово', word)
input('\n\nНажмите Enter, чтобы выйти.')