
Players
------------------
- [x] Store and retrieve player stats in DB.
- [x] Store local stats as a nested dictionary
- [ ] Write a function that adds the default stats for a new game to every player db row.

Games
------------------
- [ ] Finish Blackjack
  - [ ] doubleDown()
    - [ ] Make sure the user has enough money to double their bet
  - [ ] split()
    - [ ] Make sure the user has enough money to split their bet
    - [x] Split 1 hand into 2 hands
    - [x] Give player 2 turns when they split their cards
    - [x] Parse the results according to how many of the player's hands win/lose
  - [ ] UI stuff
    - [ ] Printing split hands underneath one another
    - [ ] Improving messages when player wins/loses
  - [x] dealerPullCard()

- [x] Make highest card for unlimited opponents
  - [x] Add the support for a user generated amount of opponents
  - [x] Test whether the deck refills after every game

Menu
------------------
- [ ] Backwards navigation
- [ ] Catching faulty input
  - [x] Game class
    - [x] setOpponentAmount()
    - [x] setDiceSides()
    - [x] placeBet()
  - [ ] Lobby class
    - [ ] initializeNewPlayer()
    - [ ] initializeExistingPlayer()
