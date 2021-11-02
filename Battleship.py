import random 
class Battleship():
    """ A class used to set up a battleship player. """
    game_end = False
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rows = list(range(10))
    letter_to_number = {key:value for key, value in zip(columns,rows)}
    def __init__(self):
        """ Upon initialization, user is given 5 boats of different lengths. """
        self.boats = {"Carrier":[5,], "Battleship":[4,], "Cruiser":[3,], "Submarine":[3,], "Destroyer":[2,]}

        self.end_game = False
        self.grid = {}
        self.occupied_cells = []
        self.bombings = []
        self.sunk = []
        # Create a rows x columns grid
        for number in Battleship.rows:
            for letter in Battleship.columns:
                self.grid[letter+str(number)] = False
    
    def print_grid(self, show_boats = False, playing = False):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        rows = list(range(10))

        header = "   "+" | ".join(columns) + " |\n"
        right_margin = "\n"
        left_margin = [f"{number}|" for number in rows]
        empty_cell = "   |"
        boat = " \u25A0 |"
        grid = header
        body_rows = [list(self.grid.values())[i:i+10] for i in range(0, 91, 10)]
        body_print = []

        for row in body_rows:
            string = ""
            for cell in row:
                if cell is not False and cell != "miss" and cell != "hit" and show_boats is True:
                    string += boat
                elif cell == "hit":
                    string += " x |"
                elif cell == "miss":
                    string += " ~ |"
                else:
                    string += empty_cell
            body_print.append(string)
            
        for row in rows:
            grid += left_margin[row] + body_print[row] + right_margin
        print(grid)
    
    def add_boat(self, boat_name, start, direction):
        start = start.upper()
        if direction.upper() == "H":
            end = Battleship.letter_to_number[start[0]] + self.boats[boat_name][0]
            if end not in Battleship.rows:
                return False
            else: 
                boat_pos = [f"{letter}{start[1]}" for letter in Battleship.columns[Battleship.letter_to_number[start[0]]:end]]
                if any(x in boat_pos for x in self.occupied_cells):
                    return False
                else:
                    for cell in boat_pos:
                        self.grid[cell] = True
                    self.occupied_cells.extend(boat_pos)
                    self.boats[boat_name].append(boat_pos)
                    return True
        elif direction.upper() == "V":
            end = int(start[1]) + self.boats[boat_name][0]
            if end not in Battleship.rows:
                return False
            else: 
                boat_pos = [f"{start[0]}{number}" for number in Battleship.rows[int(start[1]):end]]
                if any(x in boat_pos for x in self.occupied_cells):
                    return False
                else:
                    for cell in boat_pos:
                        self.grid[cell] = True
                    self.occupied_cells.extend(boat_pos)
                    self.boats[boat_name].append(boat_pos)
                    return True
        
    def bomb(self, cell, target_player):
        cell = cell.upper()
        if cell in self.bombings:
            return cell, "Target already chosen before."
        else:
            if target_player.grid[cell]: # Theres a boat on that grid
                self.bombings.append(cell)
                target_player.grid[cell] = "hit" 
                for key, value in target_player.boats.items(): # Need to take a life out of the boat
                    if cell in value[1]:
                        value[1].remove(cell)
                        if len(value[1]) == 0:
                            self.sunk.append(key)
                            if len(self.sunk) == 5:
                                print("THE GAME IS FINISHED!")
                                Battleship.game_end = True
                    else:
                        continue
                return cell, "HITED!"
            else:
                self.bombings.append(cell)
                target_player.grid[cell] = "miss"
                return cell, "MISSED!"

class Play:
    player_1 = Battleship()
    cpu = Battleship()
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rows = list(range(10))
    def cpu_setup(self):
        for boat in Play.cpu.boats.keys():
            flag = False
            while not flag:
                flag = Play.cpu.add_boat(boat, self.random_cell(), random.choice(["H", "V"]))
    
    def random_cell(self):
        return "".join([random.choice(Play.columns),str(random.choice(Play.rows))])
    
    def player_setup(self):
        print("WELCOME TO BATTLESHIP")
        print("You will be playing against CPU")
        print("You have five boats:\n    Carrier (5)\n    Battleship (4)\n    Cruiser (3)\n    Submarine (3)\n    Destroyer (2)")
        print("\n")
        Play.player_1.print_grid(True)
        for boat in Play.player_1.boats.keys():
            flag = False
            start_cell = input(f"Enter first coordinate (e.g. B4) for the {boat}: ")
            direction = input(f"Enter H to place {boat} horizonally or V to place {boat} Vertical: ")
            while not Play.player_1.add_boat(boat, start_cell, direction):
                print("!!! Boat does not fit. Please input different coordinate and/or direction !!!")   
                start_cell = input(f"Enter first coordinate (e.g. B4) for the {boat}: ")
                direction = input(f"Enter H to place {boat} horizonally or V to place {boat} Vertical: ")    
            Play.player_1.print_grid(True)

    def play(self):
        while not Play.player_1.game_end:
            print(f"CPU boats left: {5-len(Play.player_1.sunk)}")
            print(f"Player boats left: {5-len(Play.cpu.sunk)}")
            cell, msg = Play.cpu.bomb(self.random_cell(), Play.player_1)
            while msg == "Target already chosen before." or cell == None:
                cell, msg = Play.cpu.bomb(self.random_cell(), Play.player_1)
            print(f"CPU bombed cell {cell}")
            print(f"It {msg}")

            targ = input("Choose cell to bomb: ")
            cell, msg = Play.player_1.bomb(targ, Play.cpu)
            while msg == "Target already chosen before." or cell is None:
                print(f"{msg}")
                targ = input("Choose cell to bomb: ")
                cell, msg = Play.player_1.bomb(targ, Play.cpu)
            print(f"{msg}")

            print("YOUR GRID")
            Play.player_1.print_grid(show_boats = True, playing = False)
            print("CPU GRID")
            Play.cpu.print_grid()
            if Play.player_1.game_end:
                break

    
