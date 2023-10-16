import random
game_over = False

def guessnumber():
    '''
    asks user for a guess
    returns a string representation of an int
    prompts user to try again if not an int
    '''
    ipt = None
    guessed = False
    while guessed == False:
        ipt = input("\nWhat is your guess? (1-9999) (X to exit)\n")

        if ipt == 'X': return ipt
        else:
            try:
                int(ipt)
                guessed = True
            except: print('bad guess')

    return ipt

def score(attempt):
    '''
    takes a number guess
    outputs feedback on the attempt
    returns the int attempt
    '''
    attempt = int(attempt)
    if attempt < game_num: print("Too low")
    elif attempt > game_num: print("Too high")
    elif attempt == game_num:
        print("********\nYou win!\n********")
    return attempt

def mastermind_score(attempt):
    '''
    takes a number guess
    outputs feedback as with a mastermind game
    returns the int attempt
    '''
    attempt = str(attempt)
    game_str= str(game_num)
    if attempt == game_str:
        print("\nYou Win!\n")
        return int(attempt)

    if len(attempt) > len(game_str):
        print("Too many digits")
        return int(attempt)
    if len(attempt) < len(game_str):
        print("Too few digits")
        return int(attempt)

    game_chars = []
    feedback = ""
    for char in game_str:
        game_chars.append(char)

    for i,char in enumerate(attempt):
        if int(char) > int(game_chars[i]):
            feedback += (f"Digit {i}: too high\n")
        elif int(char) < int(game_chars[i]):
            feedback += (f"Digit {i}: too low\n")
        else:
            feedback += (f"Digit {i} is just right\n")

    print(feedback)
    return int(attempt)

while not game_over:
    game_num = random.randint(1,9999)
    # game_num = 5427
    guess = 0
    attempt_num = 1
    print("\n\n\n\n\n\n\n\n" +
          "***************\n" +
          " Welcome To My\n" +
          "***************\n" +
          "MASTERMIND GAME\n" +
          "***************")

    while int(guess) != game_num:
        print("------" +
              f"Attempt #{attempt_num}" +
              "------")
        guess = guessnumber()

        if guess == 'X':
            print("Gave up!")
            break

        mastermind_score(guess)

        if int(guess) != game_num: 
            guess = 0
            attempt_num +=1

    again = input("Enter Y to play again \n")
    if again == 'y' or again == 'Y':
        continue
    else:
        game_over = True
