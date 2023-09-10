import random


start = input('ви запустили гру "Камінь, ножиці, папір". хочете зіграти? (ведіть + або  -):')

if start == '+':
    print("3...2...1...")
    print('якщо ви хочете закінчити гру "-"')
    print('якщо вам цікавий рахунок нажміть "с".')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камінь ножиці папір? (ведіть к, н або п): ")
        list_play = ['к', 'н', 'п']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'к' and user == 'н':
                rand_ball += 1
            if rand == 'к' and user == 'б':
                user_ball += 1
            if rand == 'н' and user == 'к':
                user_ball += 1
            if rand == 'н' and user == 'б':
                rand_ball += 1
            if rand == 'б' and user == 'н':
                user_ball += 1
            if rand == 'б' and user == 'к':
                rand_ball += 1
        elif user == 'с':
            print('Ваші бали - ', user_ball, '. Бали вашого противника - ', rand_ball, ".")
        elif user == '-':
            print('Ваші бали - ', user_ball, '. Бали вашого противника - ', rand_ball, ".")
            print('Кінець гри!')
            break
        else:
            print('Ведіть к, н або п')
            
