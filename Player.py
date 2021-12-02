import DbAPI as db
import InputFunctions as inf
class Player:
    def __init__(self, playerinfo):
        self.username = playerinfo[0]
        self.credits = playerinfo[1]
        # Fill database with playername and credits
        db.establishConnection(f'INSERT INTO playerinfo VALUES ({inf.listToQuery([self.username, str(self.credits)])})', 'write')
        # Fill database with stats for each game
        for game in ['highestcard', 'blackjack', 'dicetoss']:
            db.establishConnection(f'INSERT INTO playerstats VALUES ({inf.listToQuery([self.username, game, 0, 0, 0, 0.0])})', 'write')

        self.statistics = db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}"', 'read')
        print()
        """
        self.statistics = {'highestcard' : [0, 0, 0, 0.0], #[Wins, losses, total games, winrate]
                           'blackjack'   : [0, 0, 0, 0.0], #[Wins, losses, total games, winrate]
                           'dicetoss'    : [0, 0, 0, 0.0]} #[Wins, losses, total games, winrate]
        # Dictionary with e.g. Blackjack: 0.3
        """

    def changeCredits(self, amt, opponentamt, changetype):
        if changetype == 'add':
            self.credits += amt * opponentamt

        elif changetype == 'subtract':
            self.credits -= amt

        elif changetype == 'multiply':
            self.credit *= amt

        db.establishConnection(f'UPDATE playerinfo SET credits = {self.credits} WHERE username = "{self.username}"','write')

    def getCredits(self):
        return self.credits

    def updateStats(self, game, wingained):
        # Check if player won or lost and update db stats for wins/losses
        if wingained:
            self.statistics[game][0] += 1
            db.establishConnection(f'UPDATE playerstats SET wins = {self.statistics[game][0]} WHERE username = "{self.username}" AND gamename = "{game}"', 'write')
        else:
            self.statistics[game][1] += 1
            db.establishConnection(f'UPDATE playerstats SET losses = {self.statistics[game][1]} WHERE username = "{self.username}" AND gamename = "{game}"', 'write')
        # Increase total games
        self.statistics[game][2] += 1

        # Calculate winrate
        winrate = (self.statistics[game][0] / self.statistics[game][2]) * 100
        self.statistics[game][3] = winrate

        # Update total wins and winrate in db
        db.establishConnection(f'UPDATE playerstats SET totalgames = "{self.statistics[game][0]}", winrate = "{winrate}" WHERE username = "{self.username}" AND gamename = "{game}"')


    def getStats(self, game):
        output = ''
        stats = db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND game = "{game}"')
        stattypes = ['Wins', 'Losses', 'Total rounds played', 'Win ratio']
        for i, stat in enumerate(self.statistics[game]):
            output += f'{stattypes[i]}: {str(stat)}\n'

        return output

    def getWinRate(self):
        return db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND ', 'read')