import helperfunctions as hf
import side_by_side as sbs

class Blackjack:
    def __init__(self, deck, player_funds_and_bet):
        self.deck                 = deck # Deck object
        self.results              = []  # Per hand, keeps track whether the hand has won/lost
        self.player_win           = 0  # 0 Tied, 1 Win, 2 Lose
        self.split_flag           = False  # Has the player split?
        self.double_down          = [False, False]  # Has the player d_d on first or second hand
        self.dealer_hand          = [self.deck.pullRandomCard()] # List with dealer cards
        self.player_hand_1        = self.deck.pull2RandomCards() # List with player cards
        self.player_hand_1        = [[8, 'Hearts', ''], [8, 'Hearts', '']]
        self.player_hand_2        = None  # This hand is created in the event of a split action.
        self.current_hand_nr      = 1  # Keeps track of the current hand the player is playing
        self.player_funds_and_bet = player_funds_and_bet  # Used to determine whether a player can d_d and/or split

    # <func> Handles the main order of turns
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

    # <Void> Handles all of the actions during the player's turn
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

            # Is the player eligible to double down?
            can_bet = self.canBet()
            CHECK1 = round_count == 1
            CHECK2 = True not in self.double_down
            CHECK3 = can_bet[1] if self.split_flag else can_bet[0]
            if (round_count == 1) and (True not in self.double_down) and (can_bet[1] if self.split_flag else can_bet[0]):
                player_options.append('Double down')

            # Is the player eligible to split?
            if (round_count == 1) and (player_hand[0][0] == player_hand[1][0]) and (not self.split_flag):
                player_options.append('Split')


            round_count += 1

            #  Player chooses their move (see above)
            choice = hf.optionsMenu('What is your next move?', player_options)

            if self.split_flag:
                choice_option_nr = 3
            else:
                choice_option_nr = 4

            #  Hit
            if choice == 1:
                player_hand.append(self.deck.pullRandomCard())
            #  Hold
            elif choice == 2:
                holding = True
            #  Double down
            elif choice == 3:
                self.double_down[self.current_hand_nr - 1] = True
                player_hand.append(self.deck.pullRandomCard())
                if self.hasBusted(player_hand):
                    self.player_win = 2
                else:
                    hf.printBothHands(
                                    [player_hand, self.dealer_hand],
                                    [self.deck.sumCards(player_hand), self.deck.sumCards(self.dealer_hand)],
                                    player_hand_nr
                                    )
                    holding = True
            #  Split
            elif choice == 4:
                self.split()
                round_count = 1


        hf.enterToContinue()

    # <Void> Splits the player hand into 2 hands and appends a new card to each hand
    def split(self):
        self.split_flag = True
        self.player_hand_2 = [self.player_hand_1[1]]
        self.player_hand_2.append(self.deck.pullRandomCard())
        self.player_hand_1.pop()
        self.player_hand_1.append(self.deck.pullRandomCard())

    # <Void> Handles all of the actions during the dealers turn
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

    # <Bool[]>Check if a user can bet double/triple their bet (double down and/or split cards)
    # Returns [can double, can triple]
    def canBet(self):
        bool_list = []
        for i in range(2):
            if self.player_funds_and_bet[0] > (self.player_funds_and_bet[1])*(i+2):
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list

    # <Bool> Checks if the dealer has reached a soft 17
    def dealerHolds(self):
        if max(self.deck.sumCards(self.dealer_hand[:-1])) >= 17:
            return True
        return False

    # <Bool>Checks if lowest combination of card values > 21
    def hasBusted(self, hand):
        sums = self.deck.sumCards(hand)
        if min(sums) > 21:
            return True
        return False

    # <Void> Compares 1 player and the dealer hand and updates self.results
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

    # <[Bool, func, int]> Uses results and some other self.<variables> to determine whether the player wins or loses and whether their bet is multiplied
    # Returns the end of game results. (Make sure to call this function from within a return statement)
    def parseResults(self):
        multiplier = 0
        # Increase multiplier if player has doubled down
        if True in self.double_down:
            multiplier = 1
            # Set multiplier to 0 if the double down hand has pushed
            if None in self.results:
                multiplier = 0 if self.results.index(None) == self.double_down.index(True) else 1

        # If player has not split their cards
        if len(self.results) == 1:
            if self.results[0] is None:
                print('You tied')
                return [True, hf.playAgain(), 0]
            elif self.results[0]:
                print('You win')
            else:
                print('You lose')

            return [self.results[0], hf.playAgain(), 1 + multiplier]


        else:
            if self.results[0] == self.results[1] and None not in self.results:
                if True in self.double_down:
                    multiplier = 1
                # Won both hands
                if True in self.results:
                    print('You win')
                    return [True, hf.playAgain(), 2 + multiplier]
                # lose both hands
                else:
                    print('You lose')
                    return [False, hf.playAgain(), 2 + multiplier]

            # Player won 1 hand and pushed the second
            elif True in self.results and None in self.results:
                print('You win')
                return [True, hf.playAgain(), 1 + multiplier]

            # Player lose 1 hand and pushed the second
            elif False in self.results and None in self.results:
                print('You lose')
                return [False, hf.playAgain(), 1 + multiplier]

            # Player either (lose 1 and won 1) or (Both hands have the same value as the dealer)
            else:
                if True in self.double_down:
                    d_d_index = self.double_down.index(True)
                    if self.results[d_d_index]:
                        print('You won')
                    else:
                        print('You lost')
                    return [self.res ults[d_d_index], hf.playAgain(), 1]
                print('You lost one and won the other hand, congratulations, you win nothing')
                return [True, hf.playAgain(), 0]