import DbAPI as db
import miscfunctions as mf
class Player:

    # Initializes a player depending on the overload method
    def __init__(self, *args):
        # Initializes new player
        if len(args) == 3: # args = username, password, credits
            self.username = args[0][0]
            self.statistics  = None

            # Create a database row with playername and starter credits
            db.establishConnection(f'INSERT INTO playerinfo VALUES ({mf.listToQuery([self.username, args[0][1], 1000])})', 'write')

            # Fill database with stats for each game
            for game in ['highestcard', 'blackjack', 'dicetoss']:
                db.establishConnection(f'INSERT INTO playerstats VALUES ({mf.listToQuery([self.username, game, 0, 0, 0, 0.0])})', 'write')
                self.statistics.append([self.username, game, 0, 0, 0, 0.0])

        # Initializes existing player
        elif len(args) == 2:
            self.username    = args[0]
            self.usercredits = db.establishConnection(f'SELECT credits FROM playerinfo WHERE username = "{self.username}" AND password = "{args[1]}"', 'read')
            self.statistics  = db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND password = "{args[1]}"', 'read')

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
        db.establishConnection(f'UPDATE playerstats SET totalgames = "{self.statistics[game][0]}", winrate = "{winrate}" WHERE username = "{self.username}" AND gamename = "{game}"', 'write')


    def getStats(self, game):
        output = ''
        stats = db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND gamename = "{game}"', 'read')
        stattypes = ['Wins', 'Losses', 'Total rounds played', 'Win ratio']
        for i, stat in enumerate(self.statistics[game]):
            output += f'{stattypes[i]}: {str(stat[i])}\n'

        return output

    def getWinRate(self):
        return db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND ', 'read')