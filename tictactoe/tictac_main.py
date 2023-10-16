import tictac_game as ttg
import tictac_ai as tai

def draw_board(game):
    '''
    prints a text representation of game's
    game_state
    '''
    x = tuple(game.game_state)
    print("\n  A   B   C\n"+
         "-------------\
        \n| {} | {} | {} | 1\
        \n-------------\
        \n| {} | {} | {} | 2\
        \n-------------\
        \n| {} | {} | {} | 3\
        \n-------------\n\n".format(*x))

def get_input():
    '''
    accepts input for the player's move.
    only accepts (a, b, c) + (1, 2, 3)
    'X' crashes the program
    '''
    while True:
        attempt = input("Type coordinates for your next move (a1,etc.):\n")
        attempt = attempt.lower()
        if list(attempt)[0] in ['a','b','c'] and list(attempt)[1] in ['1','2','3']:
            return attempt
        elif attempt == 'X':
            raise RuntimeError

def win_ifs(win):
    if win == game_state.player_token:
        draw_board(game_state)
        print("\n!!!!!!!\nYOU WIN\n!!!!!!!\n\n\n")
        return True
    elif win == game_state.ai_token:
        draw_board(game_state)
        print("\nvvvvvvvv\nYOU LOSE\n^^^^^^^^\n\n\n")
        return True
    elif win == " ":
        draw_board(game_state)
        print("\nIt's a draw...\n\n\n")
        return True
    else:
        return False


'''
Main program script
main loop runs until player terminates
'''
while True:
    print("\n\n\n\n\n\n\n\n\n"+
          "   TIC-TAC-TOE\n" +
          "******************\n" +
          "Prepare for Battle\n" +
          "******************\n\n\n")
    token = ""
    while len(token) != 1:
        token = input("Type any character to choose your token:\n")
    game_state = ttg.TicTacGame(token)

    # game loop
    while game_state.game_over == False:
        draw_board(game_state)
        turn = False
        # player turn loop
        # if place_marker returns false, the loop continues
        while turn == False:
            location = get_input()
            turn = game_state.place_marker(location)
        win = game_state.win_check()
        # checks for win, or continues to ai turn
        game_state.game_over = win_ifs(win)
        if not game_state.game_over: # begin ai turn
            draw_board(game_state)
            input("Press enter to continue opponent's turn.")

            # ai_play = game_state.simple_ai() # <--- uses a simple random choice
            ai_play = tai.ai_choice(game_state,game_state.ai_token) # more complex algorithm
            game_state.place_marker(ai_play, game_state.ai_token)

            # checks for win or continues to player turn
            win = game_state.win_check()
            game_state.game_over = win_ifs(win)

    # ask to play again
    # in "N" break main loop
    play_again = input("Play again? (N to exit)")
    if play_again == "N" or play_again == "n":
        break
