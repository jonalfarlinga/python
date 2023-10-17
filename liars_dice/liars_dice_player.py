import random as rn
from statistics import mode
from math import floor

class Player:
    # init method(self, name, number)
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.dice = [1,2,3,4,5,6]
        self.user = True

    # method drop_dice(self, num=1)
    def drop_dice(self):
        # remove a die from dice
        self.dice.pop()
            # self.dice.pop()
        return len(self.dice)

    # method choice(self)
    def choice(self,last_bid):
        while True:
            # get input from the player
            if last_bid[0] > 0:
                print(f"The current bid is {last_bid[0]} {last_bid[1]}" +
                      f"{'s' if last_bid[0] > 1 else ''}")
            else:
                print("Yer the first bidder!")
            bid = input("Enter your bid (number, face) or call the last player a LIAR!\n>")
            # (int:num, int:face) or "liar"
            # if liar is in the input
            format_bid = bid.lower()
            format_bid = format_bid.split(sep=",")
            if "liar" in bid.lower():
                # return "liar", win
                return ("liar", last_bid[0],last_bid[1])
            # if (num, face) is in the input
            else:
                try:
                    if len(format_bid) == 2:
                        bid = (int(format_bid[0]),int(format_bid[1]))
                    # if num is greater than previous bid and face is parsable
                        # return (num, face)
                        if bid[0] > last_bid[0] and 1 <= bid[0] <= 6:
                            return bid
                    print("\n\nPlease bid a #,# (number, face) or call the last player a liar!\n")
                except:
                    print("\n\nPlease bid a #,# (number, face) or call the last player a liar!\n")

    # method roll_cup(self)
    def roll_cup(self):
        # for each die in dice:
        for i in range(len(self.dice)):
            # change the die to randint(1,6)
            self.dice[i] = rn.randint(1,6)

class AI_player(Player):
    # init method(self, number)
    def __init__(self, number):
        # rnadom names
        names = {'first': ['Shipton','Curtis','Bill','Wadley','Hewson','Lutie','Adelaide'],
                'last': ['Turner','Barbosa','Santayana','Storm','Ridley','Clayton', 'Longshore']
                }
        ran_name = rn.choice(names['first']) + " " + rn.choice(names['last'])
        super().__init__(ran_name, number)

        self.user = False

    def simple_ai(self, last_bid):
        choice_list = [(last_bid[0]+1,last_bid[1]),
                       (last_bid[0]+1,last_bid[1]),
                       (last_bid[0]+1,last_bid[1]),
                       ("liar", last_bid[0], last_bid[1])
                       ]
        bid = rn.choice(choice_list)
        if bid[0] != "liar":
            print(f"{self.name} bids {bid[0]} "+
                  f"{bid[1]}{'s' if bid[0] > 1 else ''}")
        else:
            print(f'{self.name} says "LAIR!"')
        stop = input("Aye! >")
        return bid

    # method choice(self, last_bid)
    def choice(self, last_bid):
        return self.simple_ai(last_bid)

        # dice_in_play = 0
        # for each player
            # add len(player.dice) to dice_in_play
        # hidden_dice = dice_in_play - len(self.dice)
        # safe_bid = (hidden_dice/6 round up) - 1 + self.dice where dice = bidface
        # risky_bid = (safe_bid + 16%) round up
        # if bid[0] is more than hidden_dice
            # return ("liar","liar")
        # if bid[0] is less than or equal to safe_bid
            # build a choice_list: [bid[0] + 1, face=face,
                                   #bid[0] + 1, face=mode(self.dice),
                                   #bid[0] + 1,face=mode(self.dice)
                                   # ]
        # if bid is less than risky_bid
            # build a choice_list: ["liar",
                                   #bid[0] + 1, face=face,
                                   #bid[0] + 1, face=mode of self.dice,
                                   #bid[0] + 1, face=mode of self.dice,
                                   #bid[0] + 1, face=mode of self.dice
                                   # ]
        # else
            # build a choice_list: ["liar" x10,
                                   #bid[0] + 1, face=mode of self,dice
                                   # ]
        # return rn.choice(choice_list)