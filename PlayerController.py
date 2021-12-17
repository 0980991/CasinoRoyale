from Player import *

class PlayerController:
    @classmethod
    def initializeNewPlayer(self):
        available = False
        while not available:
            username = input('Please enter your player name ')
            available = self.verifyUsernameAvailability(username)
        password = input('Please enter your password ')
        # Create player object and assign it to the current player
        return Player(''.join(username), password, 1000)

    @classmethod
    def initializeExistingPlayer(self):
        user_exists = False
        while not user_exists:
            user_credentials = hf.readUserInput(['What is your username?', 'What is your password?'])
            if db.establishConnection(f'SELECT * FROM playerinfo WHERE username = "{user_credentials[0]}" AND password = "{user_credentials[1]}"', 'read') != []:
                user_exists = True

        return Player(''.join(user_credentials[0]), user_credentials[1])

    @classmethod
    def verifyUsernameAvailability(self, username):
        if db.establishConnection(f'SELECT * FROM playerinfo WHERE username = "{username[0]}"', 'read') != []:
            print('This username is already in use, please try another')
            return False
        return True