from Battleship import *

game = Play()
game.cpu_setup()
game.player_setup()
print("Setting up the game")
print("YOUR GRID")
game.player_1.print_grid(True)
print("CPU GRID")
game.cpu.print_grid()
game.play()
print("Thanks for playing. To run again enter \" python setup.py \"")