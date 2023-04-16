
with open("player2db.txt", "r") as fileRead:
    for line in fileRead:
        gameboard = line[0:9]
        i = 0
        while(line[i] !=  ','):
            i += 1
        probs = [float(x) for x in line[i+1:].split(",")]
        if(len(gameboard) != 9):
            print("error")
        print(probs)
        