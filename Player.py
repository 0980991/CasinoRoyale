class Player:
    def __init__(self, playerinfo):
        self.username = playerinfo[0]
        self.credits = playerinfo[1]
        self.stats = playerinfo[2] # Dictionary with e.g. Blackjack: [30, 2]
                                   #                                wins loses

    def changeCredits(self, amt, changetype):
        if changetype == 'add':
            self.credits += amt

        elif changetype == 'subtract':
            self.credits -= amt

        elif changetype == 'multiply':
            self.credit *= amt

        else:
            input('This feature has not yet been implemented')

    def getCredits(self):
        return self.credits