class AsciiDice:
    def __init__(self):
        self.dice = [
            'I---------I\n'
            '|         |\n'
            '|    1    |\n'
            '|         |\n'
            'I---------I\n',
            'I---------I\n'
            '|       2 |\n'
            '|         |\n'
            '| 2       |\n'
            'I---------I\n',
            'I---------I\n'
            '|       3 |\n'
            '|    3    |\n'
            '| 3       |\n'
            'I---------I\n',
            'I---------I\n'
            '| 4     4 |\n'
            '|         |\n'
            '| 4     4 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 5     5 |\n'
            '|    5    |\n'
            '| 5     5 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 6     6 |\n'
            '| 6     6 |\n'
            '| 6     6 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 7     7 |\n'
            '| 7  7  7 |\n'
            '| 7     7 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 8  8  8 |\n'
            '| 8     8 |\n'
            '| 8  8  8 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 9  9  9 |\n'
            '| 9  9  9 |\n'
            '| 9  9  9 |\n'
            'I---------I\n'

        ]

    def getDice(self, number):
        if number > len(self.dice):
            totalspaces = (9 - len(str(number)))
            spaces = ' ' * (int(totalspaces/2) - 1)
            if totalspaces % 2 != 0:
                intdice = f'I---------I\n|{9* " "}|\n|{spaces}-{str(number)}-{spaces} |\n|{9* " "}|\nI---------I\n'
            else:
                intdice = f'I---------I\n|{9* " "}|\n|{spaces}-{str(number)}-{spaces}|\n|{9* " "}|\nI---------I\n'

            return intdice
        else:
            return self.dice[number-1]