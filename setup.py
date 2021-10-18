columns = ["A", "B", "C", "D", "E", "F", "G", "H", "J"]
rows = list(range(10))

top_row = "   "+" | ".join(columns) + " |\n"
grid = ""
for number in rows:
    grid += f"{number}|" +  "   |"*len(columns) + "\n"

print(top_row + grid)