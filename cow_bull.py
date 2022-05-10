import random


number=str(random.randint(1000,9999))
cow=0
guesse=1


def calculate_cows_and_bulls(guess_number):
    cows=0
    bulls=0
    for i in range(0,4):
        if guess_number[i]==number[i]:
            cows+=1
        elif guess_number[i] in number:
            bulls+=1
    return cows,bulls

if __name__=="_main_":
    while cow<4:
        user_number=input("guess the number:")
        cow,bull=calculate_cows_and_bulls(user_number)
        print("cows:",cow)
        print("bulls:",bull)
        if cow ==4:
            print("congratulation!!! you guessed the number",number,"in",guesse,"guesses",)
        else:
            guesse+=1