class GuessGreaterThan(Exception):
    pass
class GuessLesserThan(Exception):
    pass
stored_number=60
while True:
    try:
        user_number=int(input("Enter your guess(between 1 and 100):"))
        if user_number>stored_number:
            raise GuessGreaterThan
        if user_number<stored_number:
            raise GuessLesserThan
        else:
            print("congratulations!you have guessed the correct number:")
            break
    except GuessGreaterThan:
            print("your guess is greater than the stored number")
    except GuessLesserThan:
            print("your guess is lesser than the stored number")
    except ValueError:
            print("please enter a valid number")
            
