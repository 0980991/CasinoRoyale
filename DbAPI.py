import sqlite3 as sql
import helperfunctions as hf

def establishConnection(sql_query, access_method):
    connect = sql.connect('SystemDb.db')
    cursor = connect.cursor()  # Used to execute SQL commands

    # Run commands:
    # Creates tables if the DB file is created for the first time.
    cursor.execute('CREATE TABLE IF NOT EXISTS playerinfo('
                        'username VARCHAR(20),'
                        'password VARCHAR(20),'
                        'credits  INTEGER)')

    cursor.execute('CREATE TABLE IF NOT EXISTS playerstats('
                        'username VARCHAR REFERENCES playerinfo(username),'
                        'gamename VARCHAR,'
                        'wins INTEGER,'
                        'losses INTEGER,'
                        'totalgames INTEGER,'
                        'winrate REAL)')

    if access_method == 'write':
        cursor.execute(sql_query) # In case of "No such column error" check quote marks around values
        connect.commit()
        return

    elif access_method == 'read':
        cursor.execute(sql_query)
        return hf.dbOutputToList(cursor.fetchall())

    connect.commit()

def formatPlayerStats(raw_stats):
    col_names = getColumnNames('playerstats')
    statistics = {}
    for i, game in enumerate(raw_stats):
        statistics[game[1]] = {}
        for j, col_name in enumerate(col_names):
            statistics[game[1]][col_name] = game[j + 2]
    return statistics

def getColumnNames(table_name):
    column_names = []
    column_info = establishConnection(f'PRAGMA table_info({table_name})', 'read')
    for column in column_info:
        column_names.append(column[1])
    return column_names[2:]

### Developer queries ###

# establishConnection('DELETE FROM playerinfo WHERE username = "Joe"', 'write')
# establishConnection('DROP TABLE playerinfo', 'write')
# establishConnection('DROP TABLE playerstats', 'write')
# establishConnection('ALTER TABLE playerinfo ADD COLUMN "password VARCHAR(20)"')