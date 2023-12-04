# read input.txt

input = open("./1/input.txt", "r")
lines = input.readlines()
input.close()
total = 0
number = 0
for i in range(len(lines)):
    firstDigit = -1
    secondDigit = -1
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            if firstDigit == -1:
                firstDigit = int(lines[i][j])
            else:
                secondDigit = int(lines[i][j])
    if secondDigit == -1:
        number = int(str(firstDigit) + str(firstDigit))
    else:
        number = int(str(firstDigit) + str(secondDigit))
    total += number
print(total)