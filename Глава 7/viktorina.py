import sys, pickle, shelve


def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Невозможно открыть файл, программа будет завершена', file_name, e)
        input('Нажмите Enter, чтобы выйти')
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    nominal = next_line(the_file)
    try:
        nominal = int(nominal)
    except:
        ValueError, IndexError

    explanation = next_line(the_file)

    return category, question, answers, correct, nominal, explanation


def welcome(title):
    print('\t\tДобро пожаловать в игру викторина!')
    print('\t\t', title, '\n')


def main():
    trivia_file = open_file('questions.txt.', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-', answers[i])

        answer = input('Ваш ответ: ')
        if answer == correct:
            print('Правильно!')
            score += int(nominal)
        else:
            print('Неверно, вопрос оценивается в', nominal)
        print(explanation)
        print('Счет:', score, '\n\n')
        category, question, answers, correct, nominal, explanation = next_block(trivia_file)

    trivia_file.close()
    print('Это был последний вопрос.')
    print("На вашем счету:", score)
    #score = str(score)
    #name = str(input('Введите ваше имя'))
    #return name, score
    #records_data = shelve.open('records.dat')
    #records_data[name] = [score]
    #records_data.sync()
    #print('Рекорд пользователя', name, '-',records_data[name])
    #records_file = open_file('records.dat', 'ab+')
    #pickle.dump(name, records_file)
    #records_file.close()

    #records_file = open_file('records.dat', 'ab+')
    #name = pickle.load(records_file)
    #print(name)
    #records_file.close()

def store_high_score ():
    try:
        with open("records.dat", "rb") as f:
            high_scores = pickle.load(f)
    except FileNotFoundError:
        high_scores = []
    name = input("Как тебя зовут")
    player_score = int(input("Сколько очков?"))
    vvod = (name, player_score)
    high_scores.append(vvod)
    high_scores.sort(reverse=True)
    high_scores = high_scores[:5]

    with open("файл.dat", "wb") as f:
        pickle.dump(high_scores, f)
    f = open("файл.dat", "rb")
    show_scores = pickle.load(f)
    print(show_scores)
    f.close()

def store_high_score_txt ():
    try:
        with open("records.dat", "rb") as f:
            high_scores = pickle.load(f)
    except FileNotFoundError:
        high_scores = []
    name = input("Как тебя зовут")
    player_score = int(input("Сколько очков?"))
    vvod = (name, player_score)
    high_scores.append(vvod)
    high_scores.sort(reverse=True)
    high_scores = high_scores[:5]

    with open("файл.txt", "wb") as f:
        pickle.dump(high_scores, f)
    f = open("файл.txt", "rb")
    show_scores = pickle.load(f)
    print(show_scores)
    f.close()

main()
store_high_score_txt()