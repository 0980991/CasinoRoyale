import os
from Deck import Deck

def optionsMenu(header, options):
    # Input: List of options
    # Output: Index + 1 of the option that the user selected
    # Output: -1 if the user wants to go back in the menu
    # Makes sure that invalid input gets cancelled
    optionsMenuHeader(header)
    for i in range(len(options)):
        print(str(i+1)+'.',options[i])
    choice = input()
    if choice == 'b':
        return -1
    try:
        while int(choice) not in range(len(options)+1) or int(choice) == 0:
            print("\nInvalid option. Please try again. (1 - %s)" % len(options))
            choice = input()
    except ValueError:
        int("\nInvalid option. Please try again. (1 - %s)" % len(options))
        choice = input()
    return int(choice)

def yesNoInput(question='', default_yes=True):
    if default_yes:
        question += '(Y/n)\n'
    else:
        question += '(y/N)\n'
    user_input = input(question)

    while user_input not in ['Y', 'N', 'y', 'n', '']:
        user_input = input('Invalid input please enter y or n\n')

    if user_input == 'Y' or user_input == 'y' or (user_input == '' and default_yes):
        return True
    return False

def readUserInput(questionList):
    userinput = []
    for i, question in enumerate(questionList):
        userinput.append(input('(Press b to cancel)\n\n' + question + '\n')) ## The char escape functie zou hier aangeroepen kunnen worden
        while userinput[i] == '':
            print('This field cannot be empty')
            userinput.pop() # Removes the empty space added to list
            userinput.append(input('(Press b to cancel)\n\n' + question + '\n'))
        if userinput[i] == 'b':
            return []
    return userinput

def enterToContinue(message=''):
    input(message + '\nPlease press enter to continue...')

def pageHeader(text):
    print(f'*{(len(text)*"=")}*\n|{text}|\n*{(len(text)*"-")}*\n')

def optionsMenuHeader(text):
    print(f'{text}\n{len(text) * "-"}')

def listToQuery(valuelist):
    outputstring = '"' # double quotes needed for SQL to accept them als values
    for i, detail in enumerate(valuelist):
        if i != len(valuelist)-1:  # Adds  '", "' after every input except for the last
            outputstring += str(detail) + '", "'
        else:
            outputstring += str(detail) + '"'
    return outputstring

def formatDbRow(row, attributes):
        outputstring = (20 * '=') + '\n'
        for i, userattribute in enumerate(row):
            outputstring += attributes[i] + str(userattribute) + '\n'
        return outputstring

# Converts [(a, b, c), (d, e, f)] to [[a, b, c], [d, e, f]]
def dbOutputToList(listoftuples):
    for i, item in enumerate(listoftuples):
        listoftuples[i] = list(item)
    return listoftuples

# Prints a box of characters around a string of any length
def prettyPrint(msg):
    print(f'{6*"*"}{(len(msg)*"*")}\n'
          f'|  {msg}  |\n'
          f'{6*"*"}{(len(msg)*"*")}')


#### Specifically catered to this project ####
def playAgain(): # returns a boolean
    enterToContinue()
    os.system('cls')
    prettyPrint('Continue?')
    if yesNoInput():
        return 'continue'
    return 'quit'

def handleOutcome(outcome):
    prettyPrint(outcome[2])
    return [outcome[0], outcome[1]]

def printHand(blackjack_hand): # returns nothing
    for i in range(len(blackjack_hand)):
        prettyPrint(f'{Deck().valueToRank(blackjack_hand[i][0])} of {blackjack_hand[i][1]}')

    enterToContinue()

def printBothHands(hands, sums):
    #hands = [[[1, 'hearts', 'Ace'], [1, 'hearts', 'Ace']], [[1, 'hearts', 'Ace'], [1, 'hearts', 'Ace']]]

    #  Print player hand
    prettyPrint(f'Your hand is {sums[0]}:')
    for i, hand in enumerate(hands):
        if i == 1:
            prettyPrint(f'The dealer\'s hand is {sums[1]}:')
        for card in hand:
            if card[0] >= 10 and card[2] != '':
                print(f'{card[2]} of {card[1]}')
            else:
                print(f'{card[0]} of {card[1]}')
        print(27*'_')
        print()
