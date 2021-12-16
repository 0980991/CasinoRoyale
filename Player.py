import DbAPI as db
import helperfunctions as hf
class Player:

    # Initializes a player depending on the overload method
    def __init__(self, *args):
        # Initializes new player
        if len(args) == 3: # args = username, password, credits
            self.username = args[0][0]
            self.credits = 1000
            # Create a database row with playername and starter credits
            db.establishConnection(f'INSERT INTO playerinfo VALUES ({hf.listToQuery([self.username, args[1], 1000])})', 'write')

            # Fill database with stats for each game
            for game in ['highestcard', 'blackjack', 'dicetoss']:
                db.establishConnection(f'INSERT INTO playerstats VALUES ({hf.listToQuery([self.username, game, 0, 0, 0, 0.0])})', 'write')

            # Local player statistics will always be imported from the DB and never altered from within the program to ensure the correct format
            self.statistics = db.formatPlayerStats(
                db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}"', 'read')
            )

        # Initializes existing player
        elif len(args) == 2:
            self.username = args[0]
            self.credits = db.establishConnection(f'SELECT credits FROM playerinfo WHERE username = "{self.username}" AND password = "{args[1]}"', 'read')[0][0]
            self.statistics  = db.formatPlayerStats(
                                db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}"', 'read')
                                )

    def changeCredits(self, amt, opponent_amt, change_type):
        if change_type == 'add':
            self.credits += amt * opponent_amt

        elif change_type == 'subtract':
            self.credits -= amt

        elif change_type == 'multiply':
            self.credits *= amt

        db.establishConnection(f'UPDATE playerinfo SET credits = {self.credits} WHERE username = "{self.username}"','write')

    def getCredits(self):
        return self.credits

    def updateStats(self, game, win_gained):
        query = 'UPDATE playerstats SET '
        wins = self.statistics[game]['wins'] # Assigns 'wins' variable incase win_gained=False

        # Check for player win/loss and add this to query
        if win_gained:
            wins +=  1
            query += f'wins = {wins}, '
        else:
            losses = self.statistics[game]['losses'] + 1
            query += f'losses = {losses}, '

        # Increase totalgames and add to query
        total_games = self.statistics[game]['totalgames'] + 1
        query += f'totalgames = {total_games}, '

        # Calculate winrate and add to query
        winrate = (wins / total_games) * 100
        query += f'winrate = {winrate} '

        # Add Where clause to identify player and game
        query += f'WHERE username = "{self.username}" AND gamename = "{game}"'

        # Update player stats in database
        db.establishConnection(query, 'write')

        # Update local statistics
        self.statistics = db.formatPlayerStats(
            db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}"', 'read')
        )

    def getStats(self, game_string):
        output = ''
        gamestat = self.statistics[game_string]
        for stat in gamestat:
            output += f'{stat}: {gamestat[stat]}\n'

        return output

    def getWinRate(self):
        return db.establishConnection(f'SELECT * FROM playerstats WHERE username = "{self.username}" AND ', 'read')