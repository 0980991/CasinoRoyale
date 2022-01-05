import helperfunctions as hf
import side_by_side as sbs

class Blackjack:
    def __init__(self, deck):
        self.deck         = deck
        self.player_hand_1   = self.deck.pull2RandomCards()
        self.player_hand_2   = None  # This hand is created in the event of a split action.
        self.dealer_hand     = [self.deck.pullRandomCard()]
        self.player_win = 0 # 0 Tied, 1 Win, 2 Lose
        self.double_down = False
        self.results = []
        self.current_hand_nr = 1

    ### Return [True/False, 'continue'/'quit', {multiplier}]
    def start(self):
        self.playerMove(self.player_hand_1)
        # Player's 1st hand has busted
        if self.player_win == 2:
            hf.prettyString('Your hand has busted!')
            self.results.append(False)
            if self.player_hand_2 is None:
                return self.parseResults()

        # If the user has split their cards
        if self.player_hand_2 is not None:
            self.current_hand_nr = 2
            self.playerMove(self.player_hand_2)
            # Players second hand has busted
            if self.player_win == 2:
                hf.enterToContinue(hf.prettyString('Your second hand has busted!'))
                self.results.append(False)
                # If 2 results have been appended (implying the 1st hand busted also)
                if len(self.results) == 2:
                    return self.parseResults()

        self.dealerMove()
        # Dealer has busted
        if self.player_win == 1:
            hf.prettyPrint('Dealer has busted!')
            if self.player_hand_2 is not None:
                while len(self.results) < 2:
                    self.results.append(True)
            else:
                self.results.append(True)
            return self.parseResults()
        if not self.hasBusted(self.player_hand_1):
            self.compareHands(self.player_hand_1)
        if (self.player_hand_2 is not None) and (not self.hasBusted(self.player_hand_2)):
            self.compareHands(self.player_hand_2)

        return self.parseResults()

    def playerMove(self, player_hand):
        round_count = 1
        holding = False
        self.player_win = 0

        # Instantiates the value to pass to the print function in order to differntiate between 1st and second hand in case of split
        player_hand_nr = self.current_hand_nr

        while not holding:
            hf.printBothHands(
                              [player_hand, self.dealer_hand],
                              [self.deck.sumCards(player_hand), self.deck.sumCards(self.dealer_hand)],
                              player_hand_nr
                             )
            # Check if player has blackjack
            if 21 in self.deck.sumCards(player_hand):
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
                self.double_down = True
                player_hand.append(self.deck.pullRandomCard())
                holding = True
            #  Split
            elif choice == 4 and split_flag:
                split_flag = False
                self.split()

        hf.enterToContinue()

    def split(self):
        self.player_hand_2 = [self.player_hand_1[1]]
        self.player_hand_2.append(self.deck.pullRandomCard())
        self.player_hand_1.pop()
        self.player_hand_1.append(self.deck.pullRandomCard())

    def dealerMove(self):
        self.dealer_hand.append(self.deck.pullRandomCard())
        while (not self.dealerHolds()):
            hf.printBothHands(
                              [self.player_hand_1, self.dealer_hand],
                              [self.deck.sumCards(self.player_hand_1), self.deck.sumCards(self.dealer_hand)],
                              1
                              )
            hf.enterToContinue()

            self.dealer_hand.append(self.deck.pullRandomCard())

        self.dealer_hand.pop()
        # Dealer has busted
        if self.hasBusted(self.dealer_hand):
            self.player_win = 1

        return

    def dealerHolds(self):
        if max(self.deck.sumCards(self.dealer_hand[:-1])) >= 17:
            return True
        return False

    # Checks if lowest combination of card values > 21
    def hasBusted(self, hand):
        sums = self.deck.sumCards(hand)
        if min(sums) > 21:
            return True
        return False

    def compareHands(self, player_hand):
        player_scores = self.deck.sumCards(player_hand)
        dealer_scores = self.deck.sumCards(self.dealer_hand)

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
            self.results.append(None)

        else:
            self.results.append(True)
        return

    def parseResults(self):
        # If player has not split their cards
        if len(self.results) == 1 and not self.double_down:
            if self.results[0] is None:
                print('You tied')
                return [True, hf.playAgain(), 0]
            elif self.results[0]:
                print('You win')
            else:
                print('You lose')
            return [self.results[0], hf.playAgain(), 1]
        else:
            if self.results[0] == self.results[1] and None not in self.results:
                # Won both hands
                if True in self.results:
                    print('You win')
                    return [True, hf.playAgain(), 2]
                # lose both hands
                else:
                    print('You lose')
                    return [False, hf.playAgain(), 2]

            # Player won 1 hand and pushed the second
            elif True in self.results and None in self.results:
                print('You win')
                return [True, hf.playAgain(), 1]

            # Player lose 1 hand and pushed the second
            elif False in self.results and None in self.results:
                print('You lose')
                return [False, hf.playAgain(), 1]

            # Player either (lose 1 and won 1) or (Both hands have the same value as the dealer)
            else:
                print('You tied')
                return [True, hf.playAgain(), 0]