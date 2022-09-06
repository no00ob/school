from enum import auto
from random import randint

# Strings
victoryTextStr = "You won! {0}$"
loseTextStr = "You lost! -{0}$"
tryAgainStr = "Try again? Your balance is {0}$ "
youLostAllMoneyStr = "All money lost! Uh oh."
askForBetStr = "Input your bet. Your balance is {0}$"
firstDrawStr = "First draw was {0}"
whatAreWeWorkingTowardStr = "Goal is {0}"
drawAgainStr = "Draw another card? "
invalidStr = "That's not a valid option!"
yesses = ["yes", "y", "ye", "joo"]
nos = ["no", "n", "nope", "ei"]

# Classes
class participantData:
    cardValue = 0
    currency = 1000
    currencyBet = 0
    bet = ""
    drawnCardValue = 0
    maxBetPercent = 0.2

# Player Data
# playerData.cardValue = 0
# playerData.currency = 0
# playerData.currentBet = 0
# playerData.bet = ""
# playerData.drawnCardValue = 0
playerData = participantData()

# AI Data
#aiData.cardValue = 0
#aiData.currency = 0
#aiCurrentBet = 0
#aiData.bet = 0
#aiData.maxBetPercent = 0.2
#aiData.drawnCardValue = 0
aiData = participantData()

# Internal Game Vars
goalAmount = 21
drawAnotherCard = ""
playAgain = ""
gameEnded = False
roundEnded = False
totalBet = 0
firstDraw = True

# Main Program

def IntToCard(var):
    if (var > 9):
        var = 10
    elif (var <= 0):
        var = 1
    return var

def DrawCard():
    global playerData
    global aiData
    global goalAmount

    # Player
    playerData.drawnCardValue = randint(0,12)
    playerData.drawnCardValue = IntToCard(playerData.drawnCardValue)
    playerData.cardValue += playerData.drawnCardValue
    if (playerData.cardValue > goalAmount):
        GameResults()
    # AI
    aiData.drawnCardValue = randint(0,12)
    aiData.drawnCardValue = IntToCard(aiData.drawnCardValue)
    aiData.cardValue += aiData.drawnCardValue
    if (aiData.cardValue > goalAmount):
        GameResults()
    

def GameResults():
    global roundEnded
    global gameEnded
    global playerData
    global aiData
    global playAgain

    roundEnded = True
    if (playerData.cardValue > goalAmount | (playerData.cardValue < aiData.cardValue & aiData.cardValue <= goalAmount)):
        playerData.currency -= int(playerData.bet) + aiData.bet
        aiData.currency += aiData.bet + int(playerData.bet)
        print(loseTextStr.format(totalBet))
    elif ((playerData.cardValue > aiData.cardValue & playerData.cardValue <= goalAmount) | aiData.cardValue > goalAmount):
        playerData.currency += totalBet
        aiData.currency -= totalBet
        print(victoryTextStr.format(totalBet))
    else:
        print("Undefined!")

    if (playerData.currency <= 0):
        playerData.currency = 0
        print(youLostAllMoneyStr)
        gameEnded = True
    else:
        gameEnded = False

    if (gameEnded == False):
        playAgain = input(tryAgainStr.format(playerData.currency))

def InputInt(msg = ""):
    while True:
        try:
            if (msg == ""):
                result = int(input())
            else:
                result = int(input(msg))
            break
        except:
            print(invalidStr)
    return result

def SetBet():
    global playerData
    global aiData
    global totalBet

    print(askForBetStr.format(playerData.currency))

    playerData.bet = InputInt()
    aiMaxBet = aiData.currency * aiData.maxBetPercent
    aiMaxBet = round(aiMaxBet)
    aiMinBet = playerData.bet
    aiData.bet = randint(aiMinBet, aiMaxBet)
    totalBet = playerData.bet + aiData.bet
    print("Opponent set their bet to {0}\nTotal money on table is now {1}".format(aiData.bet, totalBet))

def Start():
    global firstDraw

    firstDraw = True
    SetBet()
    DrawCard()

def GameState():
    global firstDraw
    global drawAnotherCard
    global goalAmount
    global playerData

    if (firstDraw == True):
        print(firstDrawStr.format(playerData.drawnCardValue), whatAreWeWorkingTowardStr.format(goalAmount))
        print("Opponents first draw was {0}".format(aiData.drawnCardValue))
        firstDraw = False
    else:
        print("Card drawn was {0}\nYour total card value is {1}".format(playerData.drawnCardValue, playerData.cardValue), whatAreWeWorkingTowardStr.format(goalAmount))
        print("Opponents card drawn was {0}\nOpponents total card value is {1}".format(aiData.drawnCardValue, aiData.cardValue))

    advance = False
    while (advance == False):
        drawAnotherCard = input(drawAgainStr)
        if (yesses.__contains__(drawAnotherCard)):
            advance = True
            DrawCard()
        elif (nos.__contains__(drawAnotherCard)):
            advance = True
            GameResults()
        else:
            print(invalidStr)

def Main(args = ""):
    while (roundEnded == False):
        GameState()

Start()
Main()