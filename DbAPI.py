import sqlite3 as sql


def establishConnection(sqlquery, accessmethod):
    connect = sql.connect('SystemDb.db')
    cursor = connect.cursor()  # Used to execute SQL commands
    # Run commands:
    # Creates tables if the DB file is created for the first time.

    cursor.execute('CREATE TABLE IF NOT EXISTS playerinfo('
                        'username VARCHAR,'
                        'credits  INTEGER)')
    #cursor.execute('DROP TABLE playerstats')
    cursor.execute('CREATE TABLE IF NOT EXISTS playerstats('
                        'username VARCHAR REFERENCES playerinfo(username),'
                        'gamename VARCHAR,'
                        'wins INTEGER,'
                        'losses INTEGER,'
                        'totalgames INTEGER,'
                        'winrate REAL)')

    # Add Customer Data
    if accessmethod == 'write':
        cursor.execute(sqlquery) # In case of "No such column error" check quote marks around values
        connect.commit()
        return

    elif accessmethod == 'read':
        cursor.execute(sqlquery)
        return cursor.fetchall()

    connect.commit()