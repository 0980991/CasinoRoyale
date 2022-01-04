import helperfunctions as hf

class Blackjack:
    def __init__(self, deck):
        self.deck         = deck
        self.player_hand_1   = self.deck.pull2RandomCards()
        self.player_hand_1   = [[4, 'Spades', ''], [4, 'Hearts', '']]
        self.player_hand_2   = None  # This hand is created in the event of a split action.
        self.dealer_hand     = [self.deck.pullRandomCard()]
        self.player_win = 0 # 0 Tied, 1 Win, 2 Lose
        self.holding = False
        self.multiplier = 1
        self.double_down = False
        self.results = []
        self.last_hand = True

    def start(self):
        ### Return [True/False, 'continue'/'quit', {multiplier}]
        self.playerMove(self.player_hand_1)
        # Player has busted
        if self.player_win == 2:
            hf.prettyPrint('Your hand has busted!')
            self.results.append(False)
            if self.last_hand:
                return self.parseResults()
            # hf.enterToContinue('Your first hand has busted')


        self.dealerMove()
        # Dealer has a blackjack
        if self.player_win == 2:
            hf.prettyPrint('Dealer has blackjack, You lose!')
            self.results.append(False)
            return self.parseResults()

        # Dealer has busted
        if self.player_win == 1:
            hf.prettyPrint('Dealer has busted! You win!')
            self.results.append(True)
            return self.parseResults()

        self.compareHands()
        if self.player_win == 0:
            self.results.append(None)
            return self.parseResults()

        elif self.player_win == 1:
            self.results.append(True)
            return self.parseResults()

        self.results.append(False)
        return self.parseResults()

    def playerMove(self, player_hand):
        round_count = 1
        holding = False

        # Instantiates the value to pass to the print function in order to differntiate between 1st and second hand in case of split
        if self.last_hand:
            player_hand_nr = 1
        else:
            player_hand_nr = 2

        while not holding:
            hf.printBothHands(
                              [player_hand, self.dealer_hand],
                              [self.deck.sumCards(player_hand), self.deck.sumCards(self.dealer_hand)],
                              player_hand_nr
                             )
            # Check if player has blackjack
            if 21 in self.deck.sumCards(player_hand):
                hf.enterToContinue('You have 21')
                return
            # Check if player has busted
            if self.hasBusted(player_hand):
                self.player_win = 2
                return
            player_options = ['Hit', 'Hold']

            # Is the player eligible to double down and/or split their cards?
            if round_count == 1:
                player_options.append('Double down')

                #  Does the player hold a pair?
                if player_hand[0][0] == player_hand[1][0]:
                    player_options.append('Split')
                    split_flag = True
            round_count += 1

            #  Player chooses their move (see above)
            choice = hf.optionsMenu('What is your next move?', player_options)
            #  Hit
            if choice == 1:
                player_hand.append(self.deck.pullRandomCard())
            #  Hold
            elif choice == 2:
                holding = True

            #  Double down
            elif choice == 3:
                self.multiplier = 2
                self.double_down = True
                player_hand.append(self.deck.pullRandomCard())
                holding = True
            #  Split
            elif choice == 4 and split_flag:
                split_flag = False
                self.split()
        return player_hand

    def split(self):
        self.player_hand_2 = [self.player_hand_1[1]]
        self.player_hand_2.append(self.deck.pullRandomCard())
        self.player_hand_1.pop()
        self.player_hand_1.append(self.deck.pullRandomCard())
        self.last_hand = False
        self.playerMove(self.player_hand_2)
        self.last_hand = True

    def dealerMove(self):
        self.dealer_hand.append(self.deck.pullRandomCard())
        while (not self.dealerHolds()):
            hf.printBothHands(
                              [self.player_hand_1, self.dealer_hand],
                              [self.deck.sumCards(self.player_hand_1), self.deck.sumCards(self.dealer_hand)],
                              2
                              )
            hf.enterToContinue()

            self.dealer_hand.append(self.deck.pullRandomCard())
            # Dealer has blackjack
            if 21 in self.deck.sumCards(self.dealer_hand[:-1]):  # [:-1] Removes the card added in the line above 
                self.player_win = 2
                return
            if self.dealerHolds():
                print('holding')

        self.dealer_hand.pop()
        # Dealer has busted
        if self.hasBusted(self.dealer_hand):
            self.player_win = 1

        return

    def dealerHolds(self):
        if max(self.deck.sumCards(self.dealer_hand[:-1])) > 17:
            return True
        return False

    # Checks if lowest combination of card values > 21
    def hasBusted(self, hand):
        sums = self.deck.sumCards(hand)
        if min(sums) > 21:
            return True
        return False

    def compareHands(self):
        player_scores = self.deck.sumCards(self.player_hand_1)
        dealer_scores = self.deck.sumCards(self.dealer_hand)

        # Player has 21 or dealer has busted
        if 21 in player_scores or self.hasBusted(self.dealer_hand):
            self.results.append(True)

        # Remove scores > 21 in order to compare the final max score of each hand using max()
        for p_score in player_scores:
            if p_score > 21:
                player_scores.remove(p_score)

        for d_score in dealer_scores:
            if d_score > 21:
                dealer_scores.remove(d_score)

        # Dealer has higher cards than player
        if max(player_scores) < max(dealer_scores):
            self.results.append(False)

        elif max(player_scores) == max(dealer_scores):
            self.results.append(True)
            self.multiplier = 0
            hf.prettyPrint('Tie game!, Nobody wins')

        else:
            self.results.append(True)
        return

    def parseResults(self):
        # If player has not split their cards
        if len(self.results) == 1 and not self.double_down:
            return [self.results[0], hf.playAgain(), 1]
        else:
            # Player won both hands
            if self.results[0][0] and self.results[1][0]:
                return [True, hf.playAgain(), 2]
            # Player lost both hands
            elif not self.results[0][0] and not self.results[1][0]:
                return [False, hf.playAgain(), 1]
            # Player has won 1 and lost the other hand
            else:
                return [True, hf.playAgain(), 1]
