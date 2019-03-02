## KABUNGA
## How to play: The user will roll 5 dice. 1s are worth 100 points and 5s are worth 50 points. The user will roll 5 dice and remove the 1s and 5s how they please. 
## Once removed, the user will roll the remaining dice until the user decides to stop rolling and keep their score OR the user rolls a hand without any 1s or 5s.
## In order to 'enter' the game, you must first roll a 350. The game ends when the user reaches 10,000 points.
## Please enter 'y' for yes and 'n' for no

import dice

class Game:
    def __init__(self, total_score = 0, round_score = 0, turn = 0):
        self.total_score = total_score
        self.round_score = round_score
        self.turn = turn
### Rolls the dice
    def roll(self, dicecountupdate):
        myroll = str(dicecountupdate) + 'd6'
        self.results = dice.roll(myroll)
        self.dicecount = int(len(self.results))
        self.onescount = int(self.results.count(1))
        self.fivescount = int(self.results.count(5))
        self.possiblehold = self.fivescount + self.onescount
### Tells the program if its the first turn or not
    def turn_count(self):
        if int(self.round_score) >= 350:
            self.turn += 2
        elif int(self.round_score) < 350:
            self.round_score = 0
            self.total_score = 0
### Game Loop
    def take_turn(self):
### If there are no more dice to roll
        if not self.results:
            def keep_score(self):
                round_score = (self.hold_fives * 50) + (self.hold_ones * 100)
                self.total_score += round_score
                self.round_score += round_score
                print("\n" + 'Your TOTAL SCORE is: ' + str(
                    self.total_score) + "\n" + 'Your CURRENT SCORE for this round is: ' + str(self.round_score) + "\n")
                return self.total_score, self.round_score, round_score
            keep_score(self)
        print('You roll the dice...' + "\n" + str(self.results) + "\n")
### Game ends at score: 10000
        if self.total_score > 10000:
            def end():
                print('You have reached 10,000 points. The game is now over.')
            end()
### Deciding which dice to keep
        self.hold_ones = (0)
        self.hold_fives = (0)
        self.hold_ones = int(input('You rolled ' + str(self.onescount) + ' one(s).' + "\n" + 'How many one(s) do you want to keep? (Each 1 = 100 points)' + "\n"))
        while int(self.hold_ones) > int(self.onescount):
            self.hold_ones = int(input('You have entered an invalid number. You rolled ' + str(
                self.onescount) + ' one(s).' + "\n" + 'How many one(s) do you want to keep? (Each 1 = 100 points)' + "\n"))
            if int(self.hold_ones) <= int(self.onescount):
                break
        self.hold_fives = int(input('You rolled ' + str(self.fivescount) + ' five(s).' + "\n" + 'How many five(s) do you want to keep? (Each 5 = 50 points)' + "\n"))
        while int(self.hold_fives) > int(self.fivescount):
            self.hold_fives = int(input('You rolled ' + str(
                self.fivescount) + ' five(s).' + "\n" + 'You have entered an invalid number. How many five(s) do you want to keep? (Each 5 = 50 points)' + "\n"))
            if int(self.hold_fives) <= int(self.fivescount) or self.fivescount is int:
                break
        diceheld = int(self.hold_fives) + int(self.hold_ones)
        print(self.hold_fives, self.hold_ones)
        self.dicecountupdate = int(self.dicecount) - int(diceheld)
        self.dicecount = int(self.dicecountupdate)
        results = self.results
        onecount = int(results.count(1))
        fivecount = int(results.count(5))
        count = fivecount + onecount
### If there are no dice left to roll
        if self.dicecount == 0:
            def empty_score(self, round_score):
                round_score = (self.hold_fives * 50) + (self.hold_ones * 100)
                self.total_score += round_score
                self.round_score += round_score
                print('Your TOTAL SCORE is: ' + str(
                    self.total_score) + "\n" + 'Your CURRENT SCORE for this round is: ' + str(self.round_score) + "\n")
                return self.total_score, self.round_score, round_score
            empty_score(self, round_score=self.round_score)
            self.rollagain = input('Would you like to roll again?')
            if self.rollagain == 'y':
                def turn():
                    Game.roll(self, dicecountupdate=5)
                    Game.take_turn(self)
                turn()
            if self.rollagain == 'n':
                if self.turn == 0:
                    if self.round_score < 350:
                        print(
                            'You must roll a 350 to start. You rolled a ' + str(
                                self.round_score) + "\n")
                        self.total_score = 0
                        self.round_score = 0
                        reroll = input('Would you like to roll again?')
                        if reroll == 'y':
                            Game.roll(self, 5)
                        Game.take_turn(self)
                    if self.round_score >= 350 and self.turn == 0:
                        print(
                            'You rolled ' + str(
                                self.round_score) + "this round, congratulations you are in the game!" + "\n")
                        reroll = input('Would you like to roll again?')
                        Game.turn_count(self)
                        if reroll == 'y':
                            Game.roll(self, 5)
                        Game.take_turn(self)
                        Game.turn_count(self)
### If player chooses not to keep any dice
        if diceheld == 0:
            print("\n" + 'Your TOTAL SCORE is: ' + str(
                self.total_score) + "\n" + 'Your CURRENT SCORE for this round is: ' + str(self.round_score) + "\n")
            if self.round_score < 350 and self.turn == 0:
                print(
                    'You must roll a 350 to enter the game. You rolled a ' + str(
                        self.round_score) + "\n")
                self.total_score = 0
                self.round_score = 0
                reroll = input('Would you like to roll again?')
                if reroll == 'y':
                    Game.roll(self, 5)
                Game.take_turn(self)
            if self.round_score >= 350 and self.turn == 0:
                self.rollagain = input(
                    'You chose to keep no dice this roll. Will you roll again?')
                if self.rollagain == 'y':
                    Game.roll(self, dicecountupdate=self.dicecount)
                if self.rollagain == 'n':
                    print(diceheld)
                    def keep_score(self):
                        round_score = (self.hold_fives * 1) + (self.hold_ones * 1)
                        self.total_score += round_score
                        self.round_score += round_score
                        return self.total_score, self.round_score, round_score
                    keep_score(self)
                    print('Your TOTAL SCORE is: ' + str(
                        self.total_score) + "\n" + 'Your SCORE for this round was: ' + str(self.round_score) + "\n")
                    Game.roll(self, 5)
                    Game.take_turn(self)
### If there are more dice to roll what would the player like to do?
        if count > 0:
            self.rollagain = input('Would you like to roll again? (Your dice count is: ' + str(self.dicecount) + ')' + "\n").lower()
            if self.rollagain == 'y':
                def keep_score(self):
                    round_score = (int(self.hold_fives) * 50) + (int(self.hold_ones) * 100)
                    self.round_score += round_score
                    self.total_score += round_score
                    print("\n" + 'Your TOTAL SCORE is: ' + str(self.total_score) + "\n" + 'Your CURRENT SCORE for this round is: ' + str(self.round_score) + "\n")
                    return self.total_score, self.round_score, round_score
                keep_score(self)
                Game.roll(self, dicecountupdate=self.dicecount)
                Game.take_turn(self)
### If player does not want to roll again...
            if self.rollagain == 'n':
                if self.turn == 0:
                    print(diceheld, self.hold_fives, self.hold_ones)
                    round_score = (self.hold_fives * 50) + (self.hold_ones * 100)
                    self.total_score += int(round_score)
                    self.round_score += int(round_score)
                    print("\n" + 'Your TOTAL SCORE is: ' + str(
                            self.total_score) + "\n" + 'Your CURRENT SCORE for this round is: ' + str(
                            self.round_score) + "\n")
### ...and player's round_score is less than 350: zero out score and rull again with 5 dice
                if self.round_score < 350 and self.turn == 0:
                    print(
                        'You must roll a 350 to start. You rolled a ' + str(
                            self.round_score) + "\n")
                    self.total_score = 0
                    self.round_score = 0
                    reroll = input('Would you like to roll again?')
                    if reroll == 'y':
                        Game.roll(self, 5)
                    Game.take_turn(self)
### ...and player's round score is greater than 350: take their round score, apply it to the total score, and allow player to enter the game...
                    if self.round_score >= 350 and self.turn == 0:
                        print(
                            'You rolled ' + str(
                                self.round_score) + "this round, congratulations you are in the game!" + "\n")
                        reroll = input('Would you like to roll again?')
                        Game.turn_count(self)
                        if reroll == 'y':
                            Game.roll(self, 5)
                        Game.take_turn(self)
### If player has already entered the game, take round score and apply it to total score
                if self.turn > 0:
                    self.round_score = 0
                    def keep_score(self):
                        round_score = (self.hold_fives * 50) + (self.hold_ones * 100)
                        self.total_score += round_score
                        self.round_score += round_score
                        return self.total_score, self.round_score, round_score
                    keep_score(self)
                    print('Your TOTAL SCORE is: ' + str(self.total_score) + "\n" + 'Your SCORE for this round was: ' + str(self.round_score) + "\n")
                    Game.roll(self, 5)
                    Game.take_turn(self)
### If player does not roll any 1s or 5s...
        if 1 and 5 not in results:
### ...and they are not in the game: reroll with 5 die
                if self.turn == 0:
                    self.total_score = 0
                    self.round_score = 0
                    print(
                            'You didn\'t roll and ones or fives. The round is over and you receive no points for this round. Your total score is: ' + str(
                                self.total_score) + "\n")
                    reroll = input('Would you like to roll again?')
                    if reroll == 'y':
                        Game.roll(self, 5)
                    Game.take_turn(self)
                    if reroll == 'n':
                        print('You didn\'t roll and ones or fives. The round is over and you receive no points for this round. Your total score is: ' + str(self.total_score) + "\n")
                        def turn():
                            Game.roll(self, 5)
                            Game.take_turn(self)
                        turn()
### ...and they are in the game: attribute zero to current score, show total score and live again
                if self.turn > 0:
                    self.round_score = 0
                    print(
                            'You didn\'t roll and ones or fives. The round is over and you receive no points for this round. Your total score is: ' + str(
                                self.total_score) + "\n")
                    reroll = input('Would you like to roll again?')
                    if reroll == 'y':
                        Game.roll(self, 5)
                    Game.take_turn(self)
                    if reroll == 'n':
                        print('You didn\'t roll and ones or fives. The round is over and you receive no points for this round. Your total score is: ' + str(self.total_score) + "\n")
                        def turn():
                            Game.roll(self, 5)
                            Game.take_turn(self)
                        turn()

PlayGame = Game()

PlayGame.roll(5)
PlayGame.take_turn()


