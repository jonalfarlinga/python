class Game:
    # method init(self)
    def __init__(self, players):
        '''
        Game instance takes a list of
            liars_dice_player.Player variables
        defaults game_over to False
        '''
        # self.game_over = False
        self.game_over = False
        # self.players = players
        self.players = players
        self.round = True

    def roll_the_bones(self):
        '''
        causes all players generate a new sequence of random numbers
        '''
        print("\n************************\n" +
              "**Now, ye scurvy dogs,**\n" +
              "**  ROLL THEM BONES!  **\n" +
              "************************\n\n")
        for player in self.players:
            player.roll_cup()

    def drop_player(self, player_number):
        '''
        removes a player according to the Player.number
        '''
        for i in range(len(self.players)):
            if player_number == self.players[i].number:
                pop = i
        print(f"{self.players[pop].name} has been knocked out of the game!\n")
        self.players.pop(pop)

    def dice_in_play(self):
        '''
        counts the number of dice in all players' dice cups
        returns int
        '''
        dice = 0
        for player in self.players:
            for die in player.dice:
                dice += 1
        return dice
