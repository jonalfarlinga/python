import random as rn

class TicTacGame:
    def __init__(self, player_token='X'):
        '''
        Game state stores the tokens each player uses, the current position of
        tokens in play, the status of game over, and the dict for changng
        coords and list positions.
        '''
        self.player_token = player_token
        if player_token == 'O' or player_token == 'o':
            self.ai_token = 'X'
        else:
            self.ai_token = 'O'
        self.game_state = [" ", " ", " ",
                           " ", " ", " ",
                           " ", " ", " "] 
        self.game_over = False
    
    def location_changer(self, loc):
        '''
        given a board coordinate loc, returns the index
        given an index, returns the board coordinates
        '''
        loc_dict = {'a1':0,
                    'b1':1,
                    'c1':2,
                    'a2':3,
                    'b2':4,
                    'c2':5,
                    'a3':6,
                    'b3':7,
                    'c3':8}
        if type(loc)==int:
            value = {i for i in loc_dict if loc_dict[i]==loc}
            return value
        elif type(loc)==str:
            return loc_dict[loc]
        else:
            raise ValueError
        
    def ai_option(self):
        ''' 
        creates and returns an array of all the
        indices in game_state where there is no token
        '''
        indx = []
        for i in range(9):
            if self.game_state[i] == " ":
                indx.append(i)
        return indx
        
    def place_marker(self, location, token=None):
        '''
        takes a board location and a token
        adds the token to the game_state location
        if no token entered, uses self.player_token
        returns True if the state was changed, or False if it failed.
        '''
        if token==None: token = self.player_token
        if type(location)==str:
            location = location.lower()
            location = self.location_changer(location)
        if self.game_state[location] == " ":
            self.game_state[location] = token
            return True
        else:
            print(f"{self.game_state[location]} has already been placed there!\n")
            return False
    
    def win_check(self, gs=None):
        '''
        checks the game_state for three in a row
        returns the winning token if there is,
        or returns False if no winner
        can take a Game.game_state as input, or uses self.game_state
        '''
        if gs == None:
            gs = self.game_state
        for i in [0,3,6]:
            if gs[i]==gs[i+1]==gs[i+2]:
                if gs[i] != " ": return gs[i]
        for i in [0,1,2]:
            if gs[i]==gs[i+3]==gs[i+6]:
                if gs[i] != " ": return gs[i]
        if gs[0]==gs[4]==gs[8]:
            if gs[0] != " ": return gs[0]
        if gs[2]==gs[4]==gs[6]:
            if gs[2] != " ": return gs[2]
        empty = [x for x in gs if x == " "]
        if len(empty) < 1:
            return " "
        return False
    
    def simple_ai(self):
        '''
        find the play options and select one at random
        '''
        ai_options = self.ai_option()
        return rn.choice(ai_options)
    
    def copy(self):
        '''
        returns a copy of the invoking TicTacGame instance
        '''
        copy = TicTacGame()
        copy.player_token = self.player_token
        copy.ai_token = self.ai_token
        copy.game_state = self.game_state.copy()
        copy.game_over = self.game_over
        return copy