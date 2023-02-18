# we understand a programming language by practicing what we have studied and with time we become better.
def password_game():
    password: str = 'jesus'  # the  password game will be more interesting among friends
    trials_number = 1
    guess_password = ''

    while True and trials_number < 4:  # the while is an infinite loop hence the < tells it to loop through three times
        trials_number += 1  # after ever guess one is added to the trial number hence we will have 3 guesses
        guess_password = input('enter a password')
        if guess_password == password:
            print(f"{password} is amazing")
            print('you won a sum of 1000frs')
            break



    else:
        print(f"{password} is the password")
        print('you owe me 500frs')












