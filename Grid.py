class Grid():
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rows = list(range(10))
    letter_to_number = {key:value for key, value in zip(columns,rows)}
    def __init__(self):
        self.boats = {"Carrier":[5,5,"",""], "Battleship":[4,4,"",""], "Cruiser":[3,3,"",""], "Submarine":[3,3,"",""], "Destroyer":[2,2,"",""]}
        self.grid = {}
        for number in Grid.rows:
            for letter in Grid.columns:
                self.grid[letter+str(number)] = False
    
    def add_boat(self, boat_name, start, direction):
        if direction == "Horizontal":
            end = Grid.letter_to_number[start[0]] + self.boats[boat_name][0]
            if end not in Grid.rows:
                return False
            else: 
                occupied_cells = [f"{letter}{start[1]}" for letter in Grid.columns[Grid.letter_to_number[start[0]]:end]]
                for cell in occupied_cells:
                    self.grid[cell] = True
                return True
        elif direction == "Vertical":
            end = int(start[1]) + self.boats[boat_name][0]
            if end not in Grid.rows:
                return False
            else: 
                occupied_cells = [f"{start[0]}{number}" for number in Grid.rows[int(start[1]):end]]
                for cell in occupied_cells:
                    self.grid[cell] = True
                return True