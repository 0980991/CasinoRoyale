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

        self.player_win = True
        self.holding = False
        self.multiplier = 1

    def start(self):
        ### Return [True/False, 'continue'/'quit', {multiplier}]
        self.playerMove()
        # Player has busted
        if not self.player_win:
                hf.prettyPrint('You\'ve busted! Dealer wins!')
                return [False, hf.playAgain(), self.multiplier]

        self.dealerMove()
        # Dealer has a blackjack
        if not self.player_win:
            hf.prettyPrint('Dealer has blackjack, You lose!')
            return [False, hf.playAgain(), self.multiplier]

        self.compareHands()
        return [self.player_win, hf.playAgain(), self.multiplier]

    def playerMove(self):
        while not self.holding:
            hf.printBothHands([self.player_hand, self.dealer_hand])
            player_options = ['Hit', 'Hold']

            # Is the player eligible to double down and/or split their cards?
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
                self.player_hand.append(self.deck.pullRandomCard())
            #  Hold
            elif choice == 2:
                self.holding = True

            #  Double down
            elif choice == 3:
                self.multiplier = 2
                self.player_hand.append(self.deck.pullRandomCard())
                self.holding = True
            #  Split
            elif choice == 4 and split_flag:
                split_flag = False
                self.split()
            # Player busts
            if self.hasBusted(self.player_hand):
                self.player_win = False
                return

    def split(self):
        pass

    def dealerMove(self):
        self.dealer_hand.append(self.deck.pullRandomCard())

        while (not self.dealerHolds()) or (not self.hasBusted(self.dealer_hand)):
            if self.deck.sumCards(self.dealer_hand) == 21:
                self.player_win = False
            self.dealer_hand.append(self.deck.pullRandomCard())
            hf.printBothHands([self.player_hand, self.dealer_hand[0]])

    def dealerHolds(self):
        if min(self.deck.sumCards(self.dealer_hand)) >= 17:
            return True
        return False

    # Checks if lowest combination of card values > 21
    def hasBusted(self, hand):
        sums = self.deck.sumCards(hand)
        if min(sums) > 21:
            return True
        return False

    def compareHands(self):
        player_scores = self.deck.sumCards(self.player_hand).sort()
        dealer_scores = self.deck.sumCards(self.dealer_hand).sort()

        # Player has 21 or dealer has busted
        if 21 in player_scores or self.hasBusted(self.dealer_hand):
                hf.prettyPrint('YOU WIN')
                return

        # Remove scores > 21 in order to compare the final max score of each hand using max()
        for p_score in player_scores:
            if p_score < 21:
                player_scores.remove(p_score)

        for d_score in dealer_scores:
            if d_score < 21:
                dealer_scores.remove(d_score)

        # Dealer has higher cards than player
        if max(player_scores) < max(dealer_scores):
            hf.prettyPrint('Dealer has higher card values, you lose!')
            self.player_win = False

        elif max(player_scores) == max(dealer_scores):
            hf.prettyPrint('Tie game!, Nobody wins')
            self.player_win = None

        else:
            hf.prettyPrint('Congratulations you win!!')

        return
