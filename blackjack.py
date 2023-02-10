import random

def random():
    import random
    generated = random.randint(1,13)
    return generated

cash = 100
bet = 0
cards = []
dealercards = []

def checkBust():
    global cards
    global cash 
    global bet
    global dealercards
    
    if (sum(cards) > 21):
        print("You've gone bust! You had a total of " + str(sum(cards)))
        cash = cash - bet
        theGame()

def gameReset():
    global cards
    global dealercards
    cards = []
    dealercards = []
        
def addCard():
    cards.append(random())
    checkBust()
    
def addDealerCard():   
    dealercards.append(random())
    
def addDealerOtherCards():
    global cards
    global cash 
    global bet
    global dealercards
    
    dealercards.append(random())
    print("Dealer drew " + str(dealercards[-1]))
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
    
    if sum(dealercards) == sum(cards):
        print("Tie!")
        print("You both had: " + str(sum(cards)))
        theGame()
    elif sum(dealercards) > sum(cards):
        print("Dealer wins!")
        print("You had: " + str(sum(cards)))
        print("Dealer had: " + str(sum(dealercards)))
        cash = cash - bet
        theGame()
    else:
        print("You win!")
        print("You had: " + str(sum(cards)))
        print("Dealer had: " + str(sum(dealercards)))
        cash = cash + bet
        theGame()
    
def addCardQuestion():
    question = input("Do you want another card? (y/n): ")
    if question == "y":
        addCard()
        cardList()
        addCardQuestion()
    elif question == "n":
        return
    else:
        print("Unsupported symbol")

def cardList():   
    print("Your cards are: " + str(cards) + ", total: " + str(sum(cards)))

running = 1

def theGame():
    gameReset()
    global bet
    
    bet = int(input("How much do you want to bet? (Cash: "+str(cash)+") "))
    if cash < bet:
        print("Not enough money!")
        theGame()
    
    addCard()
    addCard()
    cardList()
    addDealerCard()
    print("Dealers card is: " + str(dealercards))
    addCardQuestion()
    addDealerOtherCards()

while running == 1:
    startQuestion = input("Do you want to play?? (y/n): ")
    if startQuestion == "y":
          theGame()
    elif startQuestion == "n":
        running = 0
    else:
        print("Unsupported symbol")