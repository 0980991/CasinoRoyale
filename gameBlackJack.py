import InputFunctions as inf

class BlackJack:
    def start(self, deck):
        roundcount = 1
        gamenotover = True

        playerhand = deck.pull2RandomCards()
        dealerhand = [deck.pullRandomCard()]

        while gamenotover:

            #  Print player hand
            inf.prettyPrint('Your hand is:')
            inf.printHand(playerhand)

            #  Print dealer hand
            inf.prettyPrint(f'The dealer\'s hand is:')
            inf.printHand(dealerhand)

            #  Has the player busted?
            if deck.sumCards(playerhand) > 21:
                inf.prettyPrint('YOU\'VE BUSTED')
                return [False, inf.playAgain()]

            #  Does the player have 21?
            elif deck.sumCards(playerhand) == 21:
                inf.prettyPrint('CONGRATULATIONS YOU\'VE GOT 21')
                return [True, inf.playAgain()]

            #  Is the player eligible to split their cards?
            if playerhand[0][0] == playerhand[1][0] and roundcount == 1:
                playeroptions = ['Hit', 'Hold', 'Double down', 'Split']
                splitflag = True

            else:
                playeroptions = ['Hit', 'Hold', 'Double down']

            choice = inf.optionsMenu('What is your next move?', playeroptions)
            if choice == 1:
                self.hit(playerhand, deck.pullRandomCard())

            elif choice == 2:
                playerholds = True
                self.hold()

            elif choice == 3:
                self.doubleDown()

            elif choice == 4 and splitflag:
                splitflag = False
                self.split()

            if deck.sumCards(dealerhand) <= 17:
                dealerhand.append(deck.pullRandomCard())
                if deck.sumCards(dealerhand) == 21:
                    inf.prettyPrint('DEALER HAS 21 -- YOU LOSE')
                    return [False, inf.playAgain()]

            if playerholds:
                while deck.sumCards(dealerhand) <= 17:
                    dealerhand.append(deck.pullRandomCard())

            roundcount += 1

    def hit(self, hand, card):
        hand.append(card)

    def hold(self):
        pass

    def doubleDown(self):
        pass

    def split(self, hand):
        pass





