import tictac_ai
import tictac_game

game = tictac_game.TicTacGame()
game.game_state = [" ","X"," ","O","X"," "," "," "," "]
print("\n\n\n\n\n\n--------------------------")
print(game.game_state)
print("ai_choice",tictac_ai.ai_choice(game,"O",True))

game.game_state = ["X","X"," ","O","O"," ","O"," X","X"]
print("\n--------------------------")
print(game.game_state)
print("ai_choice:",tictac_ai.ai_choice(game,"O",True))

game.game_state = ["X"," ","O","X"," "," "," "," "," "]
print("\n--------------------------")
print(game.game_state)
print("ai_choice",tictac_ai.ai_choice(game,"O",True))

game.game_state = [" "," "," "," ","X"," "," "," "," "]
print("\n--------------------------")
print(game.game_state)
print("ai_choice",tictac_ai.ai_choice(game,"O",True))

game.game_state = [" ","O"," "," "," "," "," ","X","X"]
print("\n--------------------------")
print(game.game_state)
print("ai_choice",tictac_ai.ai_choice(game,"O",True))

game.game_state = [" ","O","X"," "," "," ","O","X","X"]
print("\n--------------------------")
print(game.game_state)
print("ai_choice",tictac_ai.ai_choice(game,"O",True))