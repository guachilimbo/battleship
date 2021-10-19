from Grid import Grid

def setup_grid(grid_dict):
    columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    rows = list(range(10))

    header = "   "+" | ".join(columns) + " |\n"
    right_margin = "\n"
    left_margin = [f"{number}|" for number in rows]
    empty_cell = "   |"
    boat = " \u25A0 |"
    grid = header
    body_rows = [list(grid_dict.values())[i:i+10] for i in range(0, 91, 10)]
    body_print = []
    for row in body_rows:
        string = ""
        for cell in row:
            if cell:
                string += boat
            else:
                string += empty_cell
        body_print.append(string)
        
    for row in rows:
        grid += left_margin[row] + body_print[row] + right_margin
    
    return grid

test = Grid()
test.add_boat("Carrier","A1","Vertical")
test.add_boat("Battleship","J4","Vertical")
test.add_boat("Cruiser","D4","Horizontal")
test.add_boat("Submarine","E5","Horizontal")
test.add_boat("Destroyer","E0","Horizontal")
print("             YOUR GRID:")
print(setup_grid(test.grid))
    