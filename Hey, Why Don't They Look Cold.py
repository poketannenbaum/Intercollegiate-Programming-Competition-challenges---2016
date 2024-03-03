from copy import copy, deepcopy
west = float(input("Enter west edge temperature: "))
east = float(input("Enter east edge temperature: "))
north = float(input("Enter north edge temperature: "))
south = float(input("Enter south edge temperature: "))
initialtemp = float(input("Enter initial interior cells temperature: "))
minutes = int(input("Enter number of minutes: "))
xcoord = int(input("Enter x-coordinate: "))
ycoord = int(input("Enter y-coordinate: "))
xrow = []
yrow = []
I = "Is epic"
counter = 0
while counter <= 9:
	yrow.append(initialtemp)
	counter += 1
counter = 0
while counter <= 9:
	xrow.append(yrow.copy())
	counter += 1
counter = 1
while counter <= 8:
	xrow[0][counter] = north
	counter +=1
counter = 1
while counter <= 8:
	xrow[9][counter] = south
	counter +=1
counter = 1
while counter <= 8:
	xrow[counter][0] = west
	counter +=1
counter = 1
while counter <= 8:
	xrow[counter][9] = east
	counter +=1
oxrow = deepcopy(xrow)
xxcounter = 1
yxcounter = 1
while minutes != -1:
	xrow[yxcounter][xxcounter] = (oxrow[yxcounter-1][xxcounter] + oxrow[yxcounter+1][xxcounter] + oxrow[yxcounter][xxcounter+1] + oxrow[yxcounter][xxcounter-1]) / 4
	xxcounter += 1
	if xxcounter == 9:
		xxcounter = 1
		yxcounter += 1
	if yxcounter == 9:
		minutes -= 1
		yxcounter = 1
		oxrow = deepcopy(xrow)
print(f"The temperature of cell {xcoord},{ycoord} is {xrow[xcoord][ycoord]}")
counter = 0
while counter <= 9:
	print(xrow[counter])
	counter += 1