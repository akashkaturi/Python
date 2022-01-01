row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
variables = input(
    "Where do you want to put the treasure?(Row,column)(seperated by commas(,)) ")
position = variables.split(',')
vertical = int(position[1])
horizontal = int(position[0])
map[vertical-1][horizontal-1] = "🚨"
print(f"\n\n\n{row1}\n{row2}\n{row3}")
