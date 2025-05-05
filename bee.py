WORDS={'PAIR':4,'HAIR':4,'CHAIR':5,'GRAPHIC':7}
def main():
    print('welcome to the game')
    print('Your letters are : A I C G P R H')
    points=0
    while len(WORDS)>0:
        print(f'{len(WORDS)} words left')
        guess=input('Guess a word: ')
        if guess=='GRAPHIC':
            WORDS.clear()
            print('Game is finished')
        elif guess in WORDS.keys():
            points+=WORDS.pop(guess)
            print(f'Good job, you earned {points} points')
    print('Game over')

main()