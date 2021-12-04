import sqlite3 as sql
import miscfunctions as mf

def establishConnection(sqlquery, accessmethod):
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


    if accessmethod == 'write':
        cursor.execute(sqlquery) # In case of "No such column error" check quote marks around values
        connect.commit()
        return

    elif accessmethod == 'read':
        cursor.execute(sqlquery)
        return mf.dbOutputToList(cursor.fetchall())

    connect.commit()




### Developer queries ###

# establishConnection('DELETE FROM playerinfo WHERE username = "Joe"', 'write')
# establishConnection('DROP TABLE playerinfo', 'write')
# establishConnection('DROP TABLE playerstats', 'write')
# establishConnection('ALTER TABLE playerinfo ADD COLUMN "password VARCHAR(20)"')