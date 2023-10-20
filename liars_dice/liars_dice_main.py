import liars_dice_game as ldg
import liars_dice_player as ldp
from os import system

# method get_dice(self, pov=None)
def get_dice(pov = None):
    '''
    returns a dictionary containing Player.number as keys and
        lists of the player's dice as values
    if pov == None, returns all dice indicated by "■"
    if pov == int, returns that player's dice as ints, and other players' as "■"
    if pov == "A", returns all dice as ints
    '''
    # dice_cups = {}
    dice_cups = {}
    # for each player
    for player in game.players:
        # if pov == None:
        if pov == 'A':
            # then dice_cups[ player.number ] is [player.dice]
            dice_cups[player.number] = player.dice
        # otherwise
        else:
            # if pov == player then dice_cups[ pov ] is [player.dice]
            if pov == player.number: dice_cups[pov] = player.dice
            # otherwise
            else:
                # make an empty dice_cups[player.number]
                dice_cups[player.number] = []
            # for each dice in player.dice
                for die in player.dice:
                    # dice_cups[player]: append "O"
                    dice_cups[player.number].append("■")
    return dice_cups

def get_players():
    '''
    asks the user for how many users are playing, how many AIs to add, and the names of Users
    instantiates players according to the inputs
    returns a list containing Players and AI_players
    '''
    safe = False
    while safe == False:
        num_users = input("How many humans are playing? (0-6)\n>")
        if num_users.isdigit() and 0 <= int(num_users) <= 6:
            num_users = int(num_users)
            safe = True
        else:
            print("\n\n***"+
                  "\nPlease enter a number between 0 and 6."+
                  "\n***\n")
    safe = False
    while safe == False:
        num_ai = input("How many pirates AARRR joining the game? (0-6)\n>")
        if num_ai.isdigit() and 0 <= int(num_ai) <= 6:
            num_ai = int(num_ai)
            safe = True
        else:
            print("\n\n***"+
                  "\nPlease enter a number between 0 and 6."+
                  "\n***\n")

    player_list = []
    for n in range(num_users):
        username = input(f"What'll we call ye, Player {n+1}? \n>")
        player_list.append(ldp.Player(username,n+1))

    for n in range(num_users, num_users + num_ai):
        player_list.append(ldp.AI_player(n+1))
    return player_list

def player_prep(button):
    '''
    takes a player who is on the button
    instructs users to look away if not on the button
    asks for input the acknowledge.
    '''
    input(f"\nPlayer {button.number} turn:" +
          f" If ye ain't {button.name}, look away!\n>")

def show_table(button_number):
    '''
    takes the player.number of the button player
    prints the table from that player's pov
    '''
    dice = get_dice(button_number)
    for player in game.players:
        print("\n\n"+ f"Player {player.number}: {player.name} has {len(player.dice)} dice.")
        print(dice[player.number],"\n")

def liar_call(button_player,bid_player,bid):
    '''
    takes the player on the button, the previous bidding player, and the last bid
    evaluates to truth of the liar claim
    the LIAR loses a die from their cup and gets dropped if dice == 0
    returns the game.players.index of the LIAR
    '''
    print("     ** LIAR IS CALLED **")
    print(f"Bid is {bid[0]} {bid[1]}{'s' if bid[0]>1 else ''}")
    show_table("A")
    die_count = 0
    for player in game.players:
        for die in player.dice:
            if die == bid[1]:
                die_count += 1
    input(f"There are {die_count} dice showing {bid[1]}")
    if bid[0] > die_count:
        print(f"{bid_player.name} is a LIAR!\n")
        in_play = bid_player.drop_dice()
        if not in_play:
            button = game.players.index(bid_player)
            game.drop_player(bid_player.number)
            return button
        return game.players.index(bid_player)
    else:
        print(f"{button_player.name} is the liar!\n")
        in_play = button_player.drop_dice()
        if not in_play:
            game.drop_player(button_player.number)
            return game.players.index(button_player)









'''
MAIN LOOP
continues until the game encounters "break"
'''
while True:
    print("\n\n\n\n\n\n\n\n"+
          "-------------------\n"+
          " I SAY YER A LIER! \n"+
          "^^^^^^^^^^^^^^^^^^^\n\n\n")

    player_list = get_players()
    game = ldg.Game(player_list)
    button = -1

    # gameplay loop
    while not game.game_over:
        if game.players == []: break     # if the player_list is empty, break the loop

        game.roll_the_bones()            # begin the round by rolling the players' dice
        # set round status variables
        game.round = True
        bid = (0,0)

        # game round loop
        while game.round:
            # increment the button first, so that it doesn't if the round == False
            button += 1

            if button >= len(game.players):
                button = 0

            player_prep(game.players[button])

            if game.players[button].user:
                show_table(game.players[button].number)

            bid = game.players[button].choice(bid,game.dice_in_play())

            if bid[0] == "liar":
                button = liar_call(game.players[button],game.players[button-1],(bid[1],bid[2]))
                game.round = False
            else:
                if game.players[button].user:
                    system('cls')

            if len(game.players) == 1:
                game.game_over = True
                print(f"\n{game.players[0].name} is the winner!")

    # ask to play again
    # in "N" break main loop
    play_again = input("Play again? (N to exit)")
    if play_again == "N" or play_again == "n":
        break
