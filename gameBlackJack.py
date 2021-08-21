import InputFunctions as inf

class BlackJack:
    def start(self, deck):
        roundcount = 1
        gamenotover = True
        playerholds = False

        playerhand = deck.pull2RandomCards()
        dealerhand = [deck.pullRandomCard()] # The dealer only shows 1 card at first

        while gamenotover:

            #  Print player hand
            inf.prettyPrint('Your hand is:')
            inf.printHand(playerhand)

            #  Has the player busted?
            if deck.sumCards(playerhand) > 21:
                inf.prettyPrint('YOU\'VE BUSTED')
                return [False, inf.playAgain()]

            #  Does the player have 21?
            elif deck.sumCards(playerhand) == 21:
                inf.prettyPrint('CONGRATULATIONS YOU\'VE GOT 21')

                return [True, inf.playAgain()]

            #  Print dealer hand
            inf.prettyPrint(f'The dealer\'s hand is:')
            inf.printHand(dealerhand)

            #  Is the player eligible to split their cards?
            if playerhand[0][0] == playerhand[1][0] and roundcount == 1:
                playeroptions = ['Hit', 'Hold', 'Double down', 'Split']
                splitflag = True

            else:
                playeroptions = ['Hit', 'Hold', 'Double down']

            #  Player chooses their move (see above)
            choice = inf.optionsMenu('What is your next move?', playeroptions)

            #  Hit
            if choice == 1:
                self.hit(playerhand, deck.pullRandomCard())

            #  Hold
            elif choice == 2:
                playerholds = True
                while deck.sumCards(dealerhand) <= 17:
                    dealerhand.append(deck.pullRandomCard())
                    deck.printHand(dealerhand)

                if self.dealerHasBusted(dealerhand, deck):
                    inf.prettyPrint('DEALER HAS BUSTED, YOU WIN')
                    return [True, inf.playAgain()]
                elif deck.sumCards(dealerhand) > deck.sumCards(playerhand):
                    inf.prettyPrint('DEALER HAS WON, YOU LOSE')
                    return [False, inf.playAgain()]
                elif deck.sumCards(dealerhand) < deck.sumCards(playerhand):
                    inf.prettyPrint('YOU HAVE WON, YOU WIN BIG MONEY BRO')
                    return [True, inf.playAgain()]
                else:
                    inf.prettyPrint('TIE, NO ONE WINS')
                    return [True, inf.playAgain()]

            #  Double down
            elif choice == 3:               # Double down
                self.doubleDown()

            #  Split
            elif choice == 4 and splitflag: # Split
                splitflag = False
                self.split()


            #  Check dealer cards
            if deck.sumCards(dealerhand) <= 17:
                dealerhand.append(deck.pullRandomCard())
                if deck.sumCards(dealerhand) == 21:
                    inf.prettyPrint('DEALER HAS 21 -- YOU LOSE')
                    return [False, inf.playAgain()]

            roundcount += 1

    def hit(self, hand, card):
        hand.append(card)

    def doubleDown(self):
        pass

    def split(self, hand):
        pass

    def dealerPullCard(self, deck):
        pass

    def dealerHasBusted(self, hand, deck):
        if deck.sumCards(hand) > 21:
            return True
        return False
