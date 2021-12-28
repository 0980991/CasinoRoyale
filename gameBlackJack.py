import helperfunctions as hf

class Blackjack:
    def __init__(self, deck, opponent_amt):
        self.deck         = deck
        self.outcome      = []
        self.gameover     = False
        self.round_count  = 1
        self.player_hand  = self.deck.pull2RandomCards()
        self.dealer_hand  = [self.deck.pullRandomCard()]
        self.player_holds = False
        self.opponent_amt = opponent_amt

        self.holding = False
        self.multiplier = 1

    def start(self):

        self.dealer_hand.append(self.deck.pullRandomCard())

        ### Return [True/False, 'continue'/'quit', {multiplier}]
        while not self.holding:
            if self.round_count == 1:
                hf.printBothHands([self.player_hand, [self.dealer_hand[0]]])
            if max(self.deck.sumCards(self.dealer_hand)) == 21:
                return [False, hf.playAgain(), self.multiplier]
            elif max(self.deck.sumCards(self.player_hand)) < 21:
                self.playerMove()
            elif min(self.deck.sumCards(self.dealer_hand)) < 17:
                self.dealerMove()
            self.round_count+=1
        if min(self.deck.sumCards(self.dealer_hand)) < 17:
            self.dealerMove()

    def playerMove(self):
        player_options = ['Hit', 'Hold']
        if self.round_count == 1:
            player_options.append('Double down')

            #  Does the player hold a pair?
            if self.player_hand[0][0] == self.player_hand[1][0]:
                player_options = ['Hit', 'Hold', 'Double down', 'Split']
                split_flag = True


        #  Player chooses their move (see above)
        choice = hf.optionsMenu('What is your next move?', player_options)
        #  Hit
        if choice == 1:
            self.hit()
        #  Hold
        elif choice == 2:
            self.holding = True
        #  Double down
        elif choice == 3:               # Double down
            self.doubleDown()
        #  Split
        elif choice == 4 and split_flag: # Split
            split_flag = False
            self.split()


    def dealerMove(self):
        self.dealer_hand.append(self.deck.pullRandomCard())
        return

        while not self.gameover:

            for card in self.deck.deck:
                print(card)

            #  Print player hand
            hf.prettyPrint('Your hand is:')
            hf.printHand(self.player_hand)

            #  Print dealer hand
            hf.prettyPrint(f'The dealer\'s hand is:')
            hf.printHand(self.dealer_hand)
            self.dealer_hand.append(self.deck.pullRandomCard())

            # Does playerhand == 21
            if self.deck.sumCards(self.player_hand) == 21:
                pass
            self.checkBlackjack()
            self.checkBusts([self.player_hand, self.dealer_hand])
            self.checkGreaterHands()

            #  Is the player eligible to split their cards?
            if self.player_hand[0][0] == self.player_hand[1][0] and self.round_count == 1:
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
            if self.deck.sumCards(self.dealer_hand) <= 17:
                self.dealer_hand.append(self.deck.pullRandomCard())

            self.round_count += 1

    def hit(self):
        self.player_hand.append(self.deck.pullRandomCard())

    def hold(self):
        self.player_holds = True
        while self.deck.sumCards(self.dealer_hand) <= 17:
            self.dealer_hand.append(self.deck.pullRandomCard())
            hf.printHand(self.dealer_hand)

    def doubleDown(self):
        self.multiplier = 2
        self.player_hand.append(self.deck.pullRandomCard())


    def split(self):
        pass

    def dealerPullCard(self):
        pass

    def hasBusted(self, hand):
        if self.deck.sumCards(hand) > 21:
            return True
        return False

    def checkGreaterHands(self):
        player_hand_greater = self.deck.firstHandGreater([self.player_hand, self.dealer_hand])
        #  Player is closer to 21 than dealer
        if player_hand_greater:
            self.outcome = [True, hf.playAgain(),'YOU HAVE WON, YOU WIN BIG MONEY']
        #  Dealer is closer to 21 than player
        elif not player_hand_greater:
            self.outcome = [False, hf.playAgain(), 'DEALER HAS WON, YOU LOSE']
        #  Game ties
        else:
            self.outcome = [None, hf.playAgain(), 'TIE, NO ONE WINS']

        self.gameover = True

    def checkBusts(self, player_dealer_hands):
        #  Player busts
        if self.hasBusted(player_dealer_hands[0]):
            self.outcome = [False, hf.playAgain(), 'YOU\'VE BUSTED']
            self.gameover = True
        #  Dealers busts
        elif self.hasBusted(player_dealer_hands[1]):
            self.outcome = [True, hf.playAgain(), 'DEALER HAS BUSTED, YOU WIN']
            self.gameover = True

    def checkBlackjack(self):
        playerhas21 = self.deck.sumCards(self.player_hand) == 21
        dealerhas21 = self.deck.sumCards(self.dealer_hand) == 21
        # Tie
        if playerhas21 and dealerhas21:
            self.outcome = [None , hf.playAgain(), 'TIE -- NO ONE WINS']
        # Dealer wins
        elif dealerhas21:
            self.outcome = [False, hf.playAgain(), 'DEALER HAS 21 -- YOU LOSE']
        # Player wins
        elif playerhas21:
            self.self.outcome = [False, hf.playAgain(), 'YOU HAVE 21 -- YOU WIN']

        if playerhas21 or dealerhas21:
            self.gameover = True


