def random():
    import random
    generated = random.randint(1,13)
    return generated

def clearScreen():
    import os
    from sys import platform
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

cash = 100
bet = 0
cardsTotal = 0
cards = []
cardsDisp = []
dealercards = []
dealercardsDisp = []

cardsvalue = {
    13: 10,
    12: 10,
    11: 10,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2,
    1: 1
}

cardfaces = {
    13: "K",
    12: "Q",
    11: "J",
    10: "10",
    9: "9",
    8: "8",
    7: "7",
    6: "6",
    5: "5",
    4: "4",
    3: "3",
    2: "2",
    1: "A"
}

def checkBust():
    global cards
    global cash 
    global bet
    global dealercards
    
    if (cardsTotal > 21):
        print("You've gone bust! You had a total of " + str(cardsTotal))
        cash = cash - bet
        theGame()

def gameReset():
    global cards
    global dealercards
    global cardsDisp
    global dealercardsDisp
    cards = []
    cardsDisp = []
    dealercards = []
    dealercardsDisp = []
    cardsTotal = 0
        
def addCard():
    global cardsTotal
    #cards.append(random())
    card = random()
    cards.append(cardsvalue.get(card))
    cardsDisp.append(cardfaces.get(card))
    print("You drew " + str(cardsDisp[-1]))
    cardsTotal = checkCardsValue()
    checkBust()
    
def checkCardsValue():
    if (1 in cards):
        if sum(cards) < 12:
            return (sum(cards) + 10)
    else:
        return sum(cards)
    
def addDealerCard():
    card = random()
    dealercards.append(cardsvalue.get(card))
    dealercardsDisp.append(cardfaces.get(card))
    
def addDealerOtherCards():
    global cards
    global cash 
    global bet
    global dealercards
    global dealercardsDisp
    
    addDealerCard()
    print("Dealer drew " + str(dealercardsDisp[-1]))
    if sum(dealercards) > 16:
        if sum(dealercards) < 22:
            checkWin()
        else:
            print("Dealer is bust, and had a total of "+str(sum(dealercards))+"! You win!")
            cash = cash + bet
            theGame()
    addDealerOtherCards()
    
def checkWin(): 
    global cards
    global cash 
    global bet
    global dealercards
    
    if sum(dealercards) == cardsTotal:
        print("Tie!")
        print("You both had: " + str(cardsTotal))
        theGame()
    elif sum(dealercards) > cardsTotal:
        print("Dealer wins!")
        print("You had: " + str(cardsTotal))
        print("Dealer had: " + str(sum(dealercards)))
        cash = cash - bet
        theGame()
    else:
        print("You win!")
        print("You had: " + str(cardsTotal))
        print("Dealer had: " + str(sum(dealercards)))
        cash = cash + bet
        theGame()

def checkBlackjackFirst():
    global cardsTotal
    global cash
    global bet
    if cardsTotal == 21:
        print("You got an instant blackjack!")
        print("Your payout is " + str(bet * 2))
        cash = cash + (bet*2)
        theGame()
        
def addCardQuestion():
    question = input("Do you want another card? (y/n): ")
    clearScreen()
    if question == "y":
        addCard()
        cardList()
        addCardQuestion()
    elif question == "n":
        return
    else:
        print("Unsupported symbol")

def cardList():
    print("Your cards are: " + str(cardsDisp) + ", total: " + str(cardsTotal))

running = 1

def theGame():
    gameReset()
    global bet
    
    bet = int(input("How much do you want to bet? (Cash: "+str(cash)+") "))
    if cash < bet:
        clearScreen()
        print("Not enough money!")
        theGame()
    
    clearScreen()
    addCard()
    addCard()
    checkBlackjackFirst()
    cardList()
    addDealerCard()
    print("Dealers card is: " + str(dealercardsDisp))
    addCardQuestion()
    addDealerOtherCards()

while running == 1:
    clearScreen()
    print("BLACKJACK (GARBAGE EDITION)")
    print("By Asbestos 2023")
    print("------------------------")
    startQuestion = input("Do you want to play?? (y/n): ")
    if startQuestion == "y":
          theGame()
    elif startQuestion == "n":
        running = 0
    else:
        print("Unsupported symbol")