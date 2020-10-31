import time
import random

random_number = random.randint(1,20)
attempts_total = 0 


print(random_number)

def print_pause(string):
    print(string)
    time.sleep(1)

def start_message():
    global attempts_total 
    print_pause("\nHello")
    print_pause("I have a fun game for you")
    print_pause("There is a number in my mind between 01 - 20 and I want you to guess it!")
    print_pause("okay?")
    while(True):
        try:
            attempts_total = int(input("\nHow many attempts do you want to guess? "))
            if attempts_total < 10 and attempts_total > 0 :
                break
            elif attempts_total > 10:
                print("\nThe maximum is 10 attempts")
            elif attempts_total < 0:
                print("\nThe minimun is 10 attempts")
        except:
            print("\nOnly numbers are allowed")
    guess()


def guess():
    global attempts_total
    if attempts_total != 0:
        print_pause(f"\nYou have {attempts_total} attempts")
        while(True):
            try:
                guessed_number = int(input("\ngo ahead and guess the number: "))
                if guessed_number > 20 or guessed_number < 0:
                    print("\nGuess only between 1 to 20")
                break
            except:
                print("Only numbers are allowed")
        attempts_total -= 1
        check_validation(guessed_number)
    else:
        losing_message()

# winning_message() method will return winning message. also use try_again() method
def winnig_message():
    print_pause("\nCONGRATOLATIONS!!!")
    print_pause("You did It :)")
    try_again()

# losing_message() method will return losing message, also use try_again() method.
def losing_message():
    print_pause("You have losed :(")
    print_pause("But it's okay you can try again")
    try_again()

# ask the user for another chance.
def try_again():
    print_pause("DO YOU WANT TO TRY AGAIN ?")
    response = input("yes or no ?\n")
    if "yes" in response.lower():
        start_message()
    else:
        print_pause("Okay see you soon :)")
        exit()         

# Checking if the guessed number is higher, lower or equal then tell the user.
def check_validation(guessed_number):
    if guessed_number == random_number:
        winnig_message()
    if guessed_number-random_number > 5:
        print_pause("You guessed way higher try lower number")
        guess()
    if guessed_number-random_number <= 5 and guessed_number-random_number > 0:
        print_pause("You guessed higher number try a little lower")
        guess()
    if guessed_number-random_number < -5:
        print_pause("You guessed way lower number try higher number")
        guess()
    if guessed_number-random_number >= -5  and guessed_number-random_number < 0:
        print_pause("You guessed lower number try a little higher")
        guess()

start_message()
