import helperfunctions as hf

class HighestCard:

    def start(self, deck, opponent_amt):
        self.deck             = deck                  # The deck
        self.player_card      = deck.pullRandomCard() # The player's card
        self.opponent_cards   = []                    # The opponent cards
        self.opponent_values  = []                    # A list of just the card values (Easier to perform arithmetic comparisons on)

        # Prevents 1v1 games to be a tie/acts as a base case when all except for 1 opponent is eliminated with tie games
        if opponent_amt == 1:
            self.opponent_cards.append(deck.pullRandomCard())
            while self.player_card[0] == self.opponent_cards[0][0]:
                self.opponent_cards[0] = deck.pullRandomCard()
            self.opponent_values.append(self.opponent_cards[0][0])
        else:
            # Fill opponents list with cards
            for i in range(opponent_amt):
                self.opponent_cards.append(deck.pullRandomCard())
                self.opponent_values.append(self.opponent_cards[i][0])

        hf.prettyPrint(f'Your hand is {deck.valueToRank(self.player_card[0])} of {self.player_card[1]}')
        hf.enterToContinue()

        # Print opponent results
        for j in range(len(self.opponent_cards)):
            hf.prettyPrint(f'Opponent {j+1}\'s card is {deck.valueToRank(self.opponent_cards[j][0])} of {self.opponent_cards[j][1]}')
            hf.enterToContinue()

            # Immediately terminate the round if an opponent has a higher card
            if self.opponent_values[j] > self.player_card[0]:
                return self.compareValues()

        return self.compareValues()

    def compareValues(self):
        maxi = max(self.opponent_values)
        if self.player_card[0] > max(self.opponent_values):
            hf.prettyPrint('You win!')
            return [True, hf.playAgain()]


        elif self.player_card[0] < max(self.opponent_values):
            hf.prettyPrint('You lose!')
            return [False, hf.playAgain()]

        else:
            nr_ties = self.opponent_values.count(max(self.opponent_values))
            hf.prettyPrint(f'{nr_ties} opponents remaining...')
            hf.enterToContinue()
            return self.start(self.deck, nr_ties)