# read input.txt

input = open("./2/input.txt", "r")
lines = input.readlines()

def resetDictionary():
	return {"red": 0, "green": 0, "blue": 0}

gameDictionary = {}
red = 12
green = 13
blue = 14

sumID = 0
sumMinimum = 0

for i in range(len(lines)):
	next = False
	gameDictionary = resetDictionary()
	line = lines[i]
	game, data = line.split(":")
	gameID = int(game.lower().split("game ")[1])
	hands = data.split(";")
	maxGreen = 1
	maxRed = 1
	maxBlue = 1
	for hand in hands:
		cubes = hand.split(",")
		gameDictionary = resetDictionary()
		for cube in cubes:
			amount, color = cube.split()
			gameDictionary[color] = int(amount)
		if gameDictionary["red"] > maxRed:
			maxRed = gameDictionary["red"]
		if gameDictionary["green"] > maxGreen:
			maxGreen = gameDictionary["green"]
		if gameDictionary["blue"] > maxBlue:
			maxBlue = gameDictionary["blue"]

	if maxRed <= red and maxGreen <= green and maxBlue <= blue:
		sumID += gameID
	product = maxRed * maxGreen * maxBlue
	sumMinimum += product
print("Sum of ID", sumID)
print("Sum of minimum", sumMinimum)