# read input.txt

numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

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
        elif lines[i][j]=="o" and j+1 < len(lines[i]) and lines[i][j+1]=="n" and j+2 < len(lines[i]) and lines[i][j+2]=="e":
            if firstDigit == -1:
                firstDigit = 1
            else:
                secondDigit = 1
        elif lines[i][j]=="t":
            if j+1 < len(lines[i]) and lines[i][j+1]=="w" and j+2 < len(lines[i]) and lines[i][j+2]=="o":
                if firstDigit == -1:
                    firstDigit = 2
                else:
                    secondDigit = 2
            elif j+1 < len(lines[i]) and lines[i][j+1]=="h" and j+2 < len(lines[i]) and lines[i][j+2]=="r" and j+3 < len(lines[i]) and lines[i][j+3]=="e" and j+4 < len(lines[i]) and lines[i][j+4]=="e":
                if firstDigit == -1:
                    firstDigit = 3
                else:
                    secondDigit = 3
        elif lines[i][j]=="f":
            if j+1 < len(lines[i]) and lines[i][j+1]=="o" and j+2 < len(lines[i]) and lines[i][j+2]=="u" and j+3 < len(lines[i]) and lines[i][j+3]=="r":
                if firstDigit == -1:
                    firstDigit = 4
                else:
                    secondDigit = 4
            elif j+1 < len(lines[i]) and lines[i][j+1]=="i" and j+2 < len(lines[i]) and lines[i][j+2]=="v" and j+3 < len(lines[i]) and lines[i][j+3]=="e":
                if firstDigit == -1:
                    firstDigit = 5
                else:
                    secondDigit = 5
        elif lines[i][j]=="s":
            if j+1 < len(lines[i]) and lines[i][j+1]=="i" and j+2 < len(lines[i]) and lines[i][j+2]=="x":
                if firstDigit == -1:
                    firstDigit = 6
                else:
                    secondDigit = 6
            elif j+1 < len(lines[i]) and lines[i][j+1]=="e" and j+2 < len(lines[i]) and lines[i][j+2]=="v" and j+3 < len(lines[i]) and lines[i][j+3]=="e" and j+4 < len(lines[i]) and lines[i][j+4]=="n":
                if firstDigit == -1:
                    firstDigit = 7
                else:
                    secondDigit = 7
        elif lines[i][j]=="e" and j+1 < len(lines[i]) and lines[i][j+1]=="i" and j+2 < len(lines[i]) and lines[i][j+2]=="g" and j+3 < len(lines[i]) and lines[i][j+3]=="h" and j+4 < len(lines[i]) and lines[i][j+4]=="t":
            if firstDigit == -1:
                firstDigit = 8
            else:
                secondDigit = 8
        elif lines[i][j]=="n" and j+1 < len(lines[i]) and lines[i][j+1]=="i" and j+2 < len(lines[i]) and lines[i][j+2]=="n" and j+3 < len(lines[i]) and lines[i][j+3]=="e":
            if firstDigit == -1:
                firstDigit = 9
            else:
                secondDigit = 9

    if secondDigit == -1:
        number = int(str(firstDigit) + str(firstDigit))
    else:
        number = int(str(firstDigit) + str(secondDigit))
    total += number
print(total)
