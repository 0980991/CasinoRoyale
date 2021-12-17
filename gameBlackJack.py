import helperfunctions as hf

class BlackJack:
    def __init__(self):
        self.deck        = None
        self.outcome     = []
        self.gameover    = False
        self.roundcount  = 1
        self.playerhand  = None
        self.dealerhand  = None
        self.playerholds = False

    def start(self, deck):
        self.deck       = deck
        self.playerhand = self.deck.pull2RandomCards()
        self.dealerhand = [self.deck.pullRandomCard()] # The dealer only shows 1 card at first

        while not self.gameover:

            #  Print player hand
            hf.prettyPrint('Your hand is:')
            hf.printHand(self.playerhand)

            #  Print dealer hand
            hf.prettyPrint(f'The dealer\'s hand is:')
            hf.printHand(self.dealerhand)

            self.checkAll()

            #  Is the player eligible to split their cards?
            if self.playerhand[0][0] == self.playerhand[1][0] and self.roundcount == 1:
                playeroptions = ['Hit', 'Hold', 'Double down', 'Split']
                splitflag = True

            else:
                playeroptions = ['Hit', 'Hold', 'Double down']

            #  Player chooses their move (see above)
            choice = hf.optionsMenu('What is your next move?', playeroptions)

            #  Hit
            if choice == 1:
                self.hit()
            #  Hold
            elif choice == 2:
                self.hold()
            #  Double down
            elif choice == 3:               # Double down
                self.doubleDown()
            #  Split
            elif choice == 4 and splitflag: # Split
                splitflag = False
                self.split()

            #  Check dealer cards
            if self.deck.sumCards(self.dealerhand) <= 17:
                self.dealerhand.append(self.deck.pullRandomCard())

            self.roundcount += 1

    def hit(self):
        self.playerhand.append(self.deck.pullRandomCard())

    def hold(self):
        self.playerholds = True
        while self.deck.sumCards(self.dealerhand) <= 17:
            self.dealerhand.append(self.deck.pullRandomCard())
            hf.printHand(self.dealerhand)


    def doubleDown(self):
        pass


    def split(self):
        pass


    def dealerPullCard(self):
        pass


    def playerHasBusted(self, hand):
        if self.deck.sumCards(hand) > 21:
            return True
        return False

    def checkGreaterHands(self):
        playerhandgreater = self.deck.firstHandGreater([self.playerhand, self.dealerhand])
        #  Player is closer to 21 than dealer
        if playerhandgreater:
            self.outcome = [True, hf.playAgain(), 'YOU HAVE WON, YOU WIN BIG MONEY']
        #  Dealer is closer to 21 than player
        elif playerhandgreater is False:
            self.outcome = [False, hf.playAgain(), 'DEALER HAS WON, YOU LOSE']
        #  Game ties
        else:
            self.outcome = [None, hf.playAgain(), 'TIE, NO ONE WINS']

        self.gameover = True

    def checkBusts(self, playerdealerhands):
        #  Player busts
        if self.playerHasBusted(playerdealerhands[0]):
            self.outcome = [False, hf.playAgain(), 'YOU\'VE BUSTED']
            self.gameover = True
        #  Dealers busts
        elif self.playerHasBusted(playerdealerhands[1]):
            self.outcome = [True, hf.playAgain(), 'DEALER HAS BUSTED, YOU WIN']
            self.gameover = True

    def checkBlackJack(self):
        playerhas21 = self.deck.sumCards(self.playerhand) == 21
        dealerhas21 = self.deck.sumCards(self.dealerhand) == 21
        if playerhas21 and dealerhas21:
            self.outcome = [None , hf.playAgain(), 'TIE -- NO ONE WINS']
        elif dealerhas21:
            self.outcome = [False, hf.playAgain(), 'DEALER HAS 21 -- YOU LOSE']
        elif playerhas21:
            self.self.outcome = [False, hf.playAgain(), 'YOU HAVE 21 -- YOU WIN OL FELLA']

        if playerhas21 or dealerhas21:
            self.gameover = True

    def checkAll(self):
        self.checkBlackJack()
        self.checkBusts([self.playerhand, self.dealerhand])
        self.checkGreaterHands()
