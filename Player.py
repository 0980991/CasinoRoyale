import DbAPI as db
import InputFunctions as inf
class Player:
    def __init__(self, playerinfo):
        self.username = playerinfo[0]
        self.credits = playerinfo[1]
         # Dictionary with e.g. Blackjack: 0.3
        db.establishConnection(f'INSERT INTO playerinfo VALUES ({inf.listToQuery([self.username, str(self.credits)])})', 'write')

    def changeCredits(self, amt, changetype):
        if changetype == 'add':
            self.credits += amt
            db.establishConnection(f'UPDATE playerstats SET highestcard = {10} WHERE username = "{self.username}"','write')

        elif changetype == 'subtract':
            self.credits -= amt

        elif changetype == 'multiply':
            self.credit *= amt

        db.establishConnection(f'UPDATE playerinfo SET credits = {self.credits} WHERE username = "{self.username}"','write')


    def getCredits(self):
        return self.credits

    def changeWinRate(self, changetype):
        pass

    def getWinRate(self):
        return db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND ', 'read')