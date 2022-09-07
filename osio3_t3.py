from random import randint

correctNumbers = [4,5,10,14,25,26,29]
ccount = 7
randNumbers = []
count = 0
iterations = 0
firstWinAfter = 0

while randNumbers != correctNumbers: # and iterations < 100
    randNumbers.clear()
    count = 0
    while count < ccount:
        newNum = randint(1,40)
        #print("newNum",newNum)
        if (randNumbers.__contains__(newNum) == False):
            randNumbers.append(newNum)
            randNumbers.sort()
            count += 1
    iterations += 1
    temp = 0
    while temp < ccount:
        if (randNumbers.__contains__(correctNumbers[temp])):
            firstWinAfter = iterations
        temp += 1

    print(iterations)
    #print("list",randNumbers)

print("Ensimmäinen voitto numero saavutettiin",firstWinAfter,"kerran jälkeen.\nJa oikea rivi saavutettiin",iterations,"kerran jälkeen.")