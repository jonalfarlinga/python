import random as rn

def ai_choice(gs, token, debug=False):
    '''
    takes a tictac_game Game and the AI's token
    returns the index for the AI's choice of play locations
    if debug=True, returns the AI's choice as well as the
    options it chose from

    The AI looks at it's own next two moves, and doesn't account
    for the opponent's moves. This was easier to code, yes, but 
    also make it possible to win.

    TicTacToe is a solved game. An exhaustive AI will always tie
    or win against a player. By not completing the algorithm,
    the AI will make mistakes, but will also capitalize on
    players' mistakes.

    If I were to complete the algorithm, first I would design a 
    similar algorithm to emulate the human player's decision. I
    add another recursive loop to examine three turns ahead, and 
    also call the player's "AI" at each iteration. The player's 
    actions should be weighted higher, so that the AI always 
    prioritizes foiling the player.
    '''
    # possible_plays stores a score for each play location
    # the index of the highest score will be the index of the
    # chosen play
    possible_plays = [0,0,0,0,0,0,0,0,0]
    game_state = gs.game_state.copy()
    # locations that are already played retain a 0, empty
    # locations get a score of 10
    for i in range(9):
        if game_state[i] == " ":
            possible_plays[i] += 10
    
    # for each possible_play if it's > 0
    # imagine a game_state where the AI fills it in and test
    # for the win and increase the score greatly if it wins
    for i in range(9):
        if possible_plays[i] > 0:
            next_state = game_state.copy()
            next_state[i] = token
            if gs.win_check(next_state) == token:
                possible_plays[i] += 4
            # for each possible_play if the location is empty
            # imagine a third game_state where the AI fills it
            # in and test for the win and increase 
            # possible_play some if it wins
            for j in range(9):
                if next_state[j] == " ":
                    third_state = next_state.copy()
                    third_state[j] = token
                    if gs.win_check(third_state) == token:
                        possible_plays[i] += 2
                        possible_plays[j] += 1
    
    # create an empty list and populate it with the indices of
    # the highest scoring possible_plays
    best_play = []
    for i in range(9):
        if possible_plays[i] == max(possible_plays):
            best_play.append(i)

    # debug return option
    if debug == True:
        return rn.choice(best_play), "best_play: "+str(best_play)
    return rn.choice(best_play)
