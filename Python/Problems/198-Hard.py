"""
[2015-01-23] Challenge #198 [Hard] Words with Enemies -- The Game! (self.dailyprogrammer)

submitted an hour ago by Coder_d00d1 3 [H]
Description:

We had an easy challenge for part 1 of this challenge.

(http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/)

To expand this further we will make a game. For this challenge you will have to create a player vs AI game battling it out with words. Following some basic rules for the games you must design and implement this game.
Rules of the Game:

    5 Turns
    Each turn the user and AI are given random letters
    The user and AI must submit a dictionary checked word derived from these letters
    The words are compared. Using the easy challenge the winner of the duel is determined by whoever has the most left over letters.
    1 point is awarded for each left over letter.
    At the end of 5 turns who ever gets the most points wins the game.

Design:

There are many unanswered design issues with this game. I leave it as part of the challenge for you to develop and decide on that design. Please keep this in mind that part of the challenge beyond solving the coding aspect of this challenge is also solving the design issue of this challenge.

Some design suggestions to consider:

    How many random letters do you get each turn? How do you determine it?
    Do you wipe all letters clean between rounds and regenerate letters or do they carry over turn to turn with a way to generate new letters?
    Do you re-use letters left over for the next turn or just ignore them?
    Does the AI searching for a word have a random level of difficulty?

AI design:

So you are giving your AI a bunch of letters. It has to find a legal word. Using a dictionary of words you can match up letters to form valid words.

Use this post to help find a dictionary to use that fits your needs (http://www.reddit.com/r/dailyprogrammer/comments/2nluof/request_the_ultimate_wordlist/)

I really like the idea of a varied AI. You can make 1-3 levels of AI. Ultimately the AI can be coded to always find the biggest word possible. This could be rather difficult for a human to play against. I would suggest developing at least 2 or 3 different levels of AI (you might have to dumb down the AI) so that players can play against an easier AI and later play against the best AI if they want more a challenge.
Checking the user input:

Users will input a word based on letters given. Your solution must check to make sure the word entered uses only the letters given to the human user but also that it makes a word in the dictionaries (see above)
Input:

Varied as needed for the game to work
Output:

Varied as needed for the game to work
Example of a UI flow:

 Welcome to Words with Enemies!
 Select an AI difficulty:
 1) easy
 2) Hard
 --> 1
 You have selected Easy! - Let's begin!

 Turn 1 -- Points You: 0 Computer: 0
 -----------------------------------------
 Your letters: a b c d e k l m o p t u
 Your word-> rekt
 I am sorry but you cannot spell rekt with your letters. Try again.
 Your letters: a b c d e k l m o p t u
 Your word-> top
 Valid Word! Open Fire!!!!
 AI selects "potluck"

 top vs potluck -- Computer wins.
 You had 0 letters left over - you score 0 points
 AI had 4 letters left over - AI score 4 points

 Turn 2 -- Points You: 0 Computer: 4
 -----------------------------------------
 Your letters: e i o k a l m q t u w y

"""

import string
import random

ai_diff = int(input("Welcome to Words with Enemies!\nSelect an AI difficulty:\n1) Easy\n2) Hard\n> "))
print("You have selected {}! - Let's begin!".format(['','Easy', 'Hard'][ai_diff]))

turn = 0
human_points = 0
ai_points = 0
while turn < 5:
    turn = turn + 1
    print("\nTurn {} - You: {}  Computer: {}\n------------------------------".format(turn, human_points, ai_points))
    possible_letters = [random.choice(string.ascii_lowercase) for x in range(0, 12)]
    print("The letters: {}".format(" ".join(possible_letters)))
    while True:
        broke = False
        found = False
        human_word = input("Your word: ")
        possible_temp = ""
        for let in possible_letters:
            possible_temp = possible_temp + let
        for char in human_word:
            if char in possible_temp:
                possible_temp = possible_temp.replace(char, "", 1)
            else:
                print("Try again, dummy. Shit ain't in the possible letters!")
                broke = True
                break
        if not broke:
            with open("american-english-insane", 'r') as dictionary:
                for line in dictionary:
                    line = line.strip()
                    if line.startswith(human_word):
                        if line == human_word:
                            print("A valid word! Let's see how this plays out.")
                            found = True
                            break
                if not found:
                    print("Try again, idiot. Shit ain't a real word.")
        if found:
            break
    # TODO word validity checking
    # TODO AI word generation
    ai_word = "".join(random.choice(possible_letters) for x in range(0, 4))
    print("The AI selects \"{}\".".format(ai_word))

    left, right = human_word, ai_word
    print("\n{} vs {}".format(left, right))
    for char in left + right:
        if char in left and char in right:
            left = left.replace(char, "", 1)
            right = right.replace(char, "", 1)

    if len(left) == len(right):
        print("It's a tie! {} vs {}\nNo points to either side.".format(left, right))
    elif len(left) > len(right):
        print("You had {} left over. {} points to you!".format(left, len(left)))
        human_points = human_points + len(left)
    else:
        print("The AI had {} left over. {} points to the AI.".format(right, len(right)))
        ai_points = ai_points + len(right)

if human_points == ai_points:
    print("\nYou're both dumb-dumbs. God, why can't either of you win?!")
elif human_points > ai_points:
    print("\nThe human player wins the whole damn game, with {} points! Good job, meatbag!".format(human_points))
else:
    print("\nHAHAHA OH WOW. Damn, human, you suck. AI wins, with {} soul-crushing points.".format(ai_points))
