import random

if __name__ == '__main__':

    userName = input('What is your name?')
    print(f'Hello {userName}')

    while True:
        numberGuess = input('Guess a number between 1-10...')


        def genRandomNum():
            outNum = random.randint(1, 11)
            return outNum


        try:
            if int(numberGuess) == genRandomNum():
                print('You win')
            else:
                print('Try again')
        except Exception:
            print('Not a number entered')
