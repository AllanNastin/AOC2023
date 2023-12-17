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

for i in range(len(lines)):
	next = False
	gameDictionary = resetDictionary()
	line = lines[i]
	game, data = line.split(":")
	gameID = int(game.lower().split("game ")[1])
	hands = data.split(";")
	for hand in hands:
		cubes = hand.split(",")
		for cube in cubes:
			amount, color = cube.split()
			gameDictionary[color] = int(amount)
		if gameDictionary["red"] > red or gameDictionary["green"] > green or gameDictionary["blue"] > blue:
			next = True
			break
	if next:
		next = False
		continue
	sumID += gameID
print("Sum of ID", sumID)