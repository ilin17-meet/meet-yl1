from meet import *
cells = []
for i in range (50):
	cell = {"x":5,"y":3,"radius":30,"dx":0.1,"dy":0}
	z=create_cell(cell)
	cells.append(z)
while True:
	move_cells(cells)