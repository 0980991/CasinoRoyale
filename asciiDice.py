class asciiDice:
    def __init__(self):
        self.dice = [
            'I---------I\n'
            '|         |\n'
            '|    0    |\n'
            '|         |\n'
            'I---------I\n',
            'I---------I\n'
            '|       0 |\n'
            '|         |\n'
            '| 0       |\n'
            'I---------I\n',
            'I---------I\n'
            '|       0 |\n'
            '|    0    |\n'
            '| 0       |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0     0 |\n'
            '|         |\n'
            '| 0     0 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0     0 |\n'
            '|    0    |\n'
            '| 0     0 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0     0 |\n'
            '| 0     0 |\n'
            '| 0     0 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0     0 |\n'
            '| 0  0  0 |\n'
            '| 0     0 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0  0  0 |\n'
            '| 0     0 |\n'
            '| 0  0  0 |\n'
            'I---------I\n',
            'I---------I\n'
            '| 0  0  0 |\n'
            '| 0  0  0 |\n'
            '| 0  0  0 |\n'
            'I---------I\n'

        ]

    def getDice(self, number):
        if number >= len(self.dice):
            totalspaces = (9 - len(str(number)))
            spaces = ' ' * int(totalspaces/2)
            if totalspaces % 2 != 0:
                intdice = f'I---------I\n|{9* " "}|\n|{spaces}{str(number)}{spaces} |\n|{9* " "}|\nI---------I\n'
            else:
                intdice = f'I---------I\n|{9* " "}|\n|{spaces}{str(number)}{spaces}|\n|{9* " "}|\nI---------I\n'

            return intdice
        else:
            return self.dice[number-1]