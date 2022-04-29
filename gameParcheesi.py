from Dice import *
import helperfunctions as hf

class gameParcheesi:

    def __init__(self, players=None, nr_opponents=0) -> None:
        self.nr_opponents = nr_opponents
        self.players = players if players is not None else []
        self.dice_hand = DiceHand(2, 6)
        self.game_modes = ['1v1', '1v2 Free for all', '2v2', '1v3 Free for all']
        self.spanish_mode = False
        self.current_player = -1
        # Board Properties:
        #   - 68 tiles
        #   - 12 safe tiles
        #
        #
        #       - [0, 7, 12, 17, 24, 31, 38, 43, 48, 55, 60]
        #
        #
        #
        #   - 28 End base tiles
        #       - 7 per player
        # Game modes:
        # 1v1 --> Opponent start square = 

    def initPlayers(self, nr_players):
        nr_opp = nr_players - 1
        if nr_opp > 3:
                nr_opp = 3
        nr_players = nr_opp + 1
        self.nr_opponents = nr_opp

        for i in range(len(nr_players)):
            self.players.append({'player_nr'   : i,
                                 'game_pieces' : [None, None, None, None],
                                 'start_tile'  : i*17
                                 })
    def start(self):
        choice = 1
        while choice > 0:
            choice = hf.optionsMenu('What game mode would you like to play?',
                                    self.game_modes)
            if choice == -1: return
            self.initPlayers(choice)

    def start(self, i_game_mode):
        self.initPlayers(i_game_mode)
        pass

    def getPlayersPostitions(self):
        positions = []
        for player in self.players:
            positions.append(player['game_pieces'])
        return positions

    def tileIsOccupied(self, tile_nr):
        p_p = self.getPlayersPostitions()
        if tile_nr in p_p and p_p.index(tile_nr)self.current_player:

        return True
    return False

    def playerTurn(self, i_player):
        p_start_tile = self.players[i_player]['start_tile']
        i_doubles = 0
        b_player_turn = True
        # 1. Roll
        while b_player_turn:
            self.dice_hand.roll()
            roll = self.dice_hand.getCurrentValues()
            if (5 in roll
                and self.playerInStartBase(i_player)
                and self.getTileInfo(self.players[i_player]['start_tile'])):

                pass
            else:
                pass

    def spawnPiece(self, i_player):
        for piece in self.players[i_player]['game_pieces']:
            if piece is None:
                piece = self.players[i_player]['start_tile']
                return
