import DbAPI
class Player:
    def __init__(self, playerinfo):
        self.username = playerinfo[0]
        self.credits = playerinfo[1]
        self.winrate = playerinfo[2] # Dictionary with e.g. Blackjack: 0.3
        DbAPI.establishConnection(f'INSERT INTO playerinfo VALUES ({advisorinfostring})', 'write')

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