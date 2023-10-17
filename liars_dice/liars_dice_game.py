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
        causes all players to roll their dice.
        '''
        print("\n************************\n" +
              "**Now, ye scurvy dogs,**\n" +
              "**  ROLL THEM BONES!  **\n" +
              "************************\n\n")
        for player in self.players:
            player.roll_cup()

    def drop_player(self, player_number):
        for i in range(len(self.players)):
            if player_number == self.player[i].number:
                print(f"{self.player[i].name} has been knocked out of the game!\n")
                self.players.pop(i)
