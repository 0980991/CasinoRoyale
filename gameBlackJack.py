import InputFunctions as inf

class BlackJack:
    def __init(self)
        self.deck = None
        self.gamenotover = True
        self.roundcount = 1
        self.playerholds = False

        self.playerhand = None
        self.dealerhand = None

    def start(self, deck):
        self.deck = deck


        self.playerhand = self.deck.pull2RandomCards()
        self.dealerhand = [self.deck.pullRandomCard()] # The dealer only shows 1 card at first

        while gamenotover:

            #  Print player hand
            inf.prettyPrint('Your hand is:')
            inf.printHand(self.playerhand)

            #  Has the player busted?
            if self.deck.sumCards(self.playerhand) > 21:
                inf.prettyPrint('YOU\'VE BUSTED')
                return [False, inf.playAgain()]

            #  Does the player have 21?
            elif self.deck.sumCards(self.playerhand) == 21:
                inf.prettyPrint('CONGRATULATIONS YOU\'VE GOT 21')

                return [True, inf.playAgain()]

            #  Print dealer hand
            inf.prettyPrint(f'The dealer\'s hand is:')
            inf.printHand(self.dealerhand)

            #  Is the player eligible to split their cards?
            if self.playerhand[0][0] == self.playerhand[1][0] and roundcount == 1:
                playeroptions = ['Hit', 'Hold', 'Double down', 'Split']
                splitflag = True

            else:
                playeroptions = ['Hit', 'Hold', 'Double down']

            #  Player chooses their move (see above)
            choice = inf.optionsMenu('What is your next move?', playeroptions)

            #  Hit
            if choice == 1:
                self.hit()

            #  Hold
            elif choice == 2:


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
                if self.deck.sumCards(self.dealerhand) == 21:
                    inf.prettyPrint('DEALER HAS 21 -- YOU LOSE')
                    return [False, inf.playAgain()]

            self.roundcount += 1

    def hit(self):
        self.playerhand.append(self.deck.pullRandomCard())

    def hold(self):
    self.playerholds = True
    while self.deck.sumCards(self.dealerhand) <= 17:
        self.dealerhand.append(self.deck.pullRandomCard())
        inf.printHand(self.dealerhand)

    if self.dealerHasBusted(self.dealerhand, self.deck):
        inf.prettyPrint('DEALER HAS BUSTED, YOU WIN')
        return [True, inf.playAgain()]
    elif self.deck.sumCards(self.dealerhand) > self.deck.sumCards(self.playerhand):
        inf.prettyPrint('DEALER HAS WON, YOU LOSE')
        return [False, inf.playAgain()]
    elif self.deck.sumCards(self.dealerhand) < self.deck.sumCards(self.playerhand):
        inf.prettyPrint('YOU HAVE WON, YOU WIN BIG MONEY BRO')
        return [True, inf.playAgain()]
    else:
        inf.prettyPrint('TIE, NO ONE WINS')
        return [True, inf.playAgain()]

    def doubleDown(self):
        pass

    def split(self):
        pass

    def dealerPullCard(self):
        pass

    def dealerHasBusted(self):
        if self.deck.sumCards(hand) > 21:
            return True
        return False
