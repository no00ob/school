from random import randint

correctNumbers = [4,5,10,14,25,26,29]
goalAmount = 7
randNumbers = []
iterations = 0

def RandomNums(goal = 0):
    tempList = []
    count = 0
    while count < goal:
        newNum = randint(1,40)
        #print("newNum",newNum)
        if (tempList.__contains__(newNum) == False):
            tempList.append(newNum)
            tempList.sort()
            count += 1
    return tempList

def CheckMatchForFirstWin(nums = [], correctNums = [], goal = 0):
    temp = 0
    while temp < goal:
        if (nums.__contains__(correctNums[temp])):
            return iterations
        temp += 1
    return 0

while randNumbers != correctNumbers: # and iterations < 100
    randNumbers.clear()
    randNumbers = RandomNums(goalAmount)
    iterations += 1
    firstWinAfter = CheckMatchForFirstWin(randNumbers, correctNumbers, goalAmount)

    print(iterations)
    #print("list",randNumbers)

print("Ensimmäinen voitto numero saavutettiin",firstWinAfter,"kerran jälkeen.\nJa oikea rivi saavutettiin",iterations,"kerran jälkeen.")