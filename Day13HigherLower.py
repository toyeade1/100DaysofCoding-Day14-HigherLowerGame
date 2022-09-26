import random
from Day13logo import logo, vs
from Day13GameData import data
def higherLower():
    game_data = data
    compare1 = random.choice(game_data)
    compare1_name = compare1['name']
    compare1_follower_count = compare1['follower_count']
    compare1_description = compare1['description']
    compare1_country = compare1['country']

    compare2 = random.choice(game_data)
    compare2_name = compare2['name']
    compare2_follower_count = compare2['follower_count']
    compare2_description = compare2['description']
    compare2_country = compare2['country']

    if compare1 == compare2:
        compare2 = random.choice(game_data)
    print(logo)
    print(f'Compare A: {compare1_name}, a {compare1_description}, from {compare1_country}')
    print(vs)
    print(f'Against B: {compare2_name}, a {compare2_description}, from {compare2_country}')

    score = 0
    followers_choice = str(input('Who has more followers? Type \'A\' or \'B\': ')).upper()
    get_it_right = False
    if followers_choice == 'A' and compare1_follower_count > compare2_follower_count:
        get_it_right = True
    elif followers_choice == 'B' and compare2_follower_count > compare1_follower_count:
        get_it_right = True
    while get_it_right:
        score += 1
        compare1 = compare2
        compare1_name = compare1['name']
        compare1_follower_count = compare1['follower_count']
        compare1_description = compare1['description']
        compare1_country = compare1['country']

        compare2 = random.choice(game_data)
        compare2_name = compare2['name']
        compare2_follower_count = compare2['follower_count']
        compare2_description = compare2['description']
        compare2_country = compare2['country']
        if compare1 == compare2:
            compare2 = random.choice(game_data)
        print(logo)
        print(f'You\'re right! Current score: {score}')
        print(f'Compare A: {compare1_name}, a {compare1_description}, from {compare1_country}')
        print(vs)
        print(f'Against B: {compare2_name}, a {compare2_description}, from {compare2_country}')

        followers_choice = str(input('Who has more followers? Type \'A\' or \'B\': ')).upper()
        get_it_right = False
        if followers_choice == 'A' and compare1_follower_count > compare2_follower_count:
            get_it_right = True
        elif followers_choice == 'B' and compare2_follower_count > compare1_follower_count:
            get_it_right = True

        else:
            get_it_right = False

    else:
        print(f'Sorry, that\'s wrong. Final score: {score} ')
    play_again = str(input('Do you want to play again? \'y\' or \'n\': ')).lower()
    if play_again == 'y':
        higherLower()
    else:
        print('Have a Good night !!')



higherLower()