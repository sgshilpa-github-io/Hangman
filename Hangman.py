import random
import sys

words = ["apprehensive", "jittery", "overcast", "damp", "laidback"]
number = random.randrange(0, 5, 1)
#print number
# print words[number]
# print words[number].__len__()
global chances
chances = words[number].__len__()+2
# print chances
solution = []
print "Welcome to guess the word game"
print "YOUR HINT! "
print "The number has "+str(len(words[number]))+ " letters in it"
print "Let's go"
letter = raw_input("Enter your letter:").lower()

while True:

        if chances >= 1:

            if len(letter) == 1:

                if letter in words[number]:
                    if letter not in solution:
                        for x in range(1, words[number].count(letter)+1):
                            solution.append(letter)
                            # print "lenth of solution" +str(len(solution))
                            if len(solution) == len(words[number]):
                                print solution
                                print "Congratulations!! You won"
                                print "The word is "+ words[number]
                                sys.exit()

                    else:
                        print "You have already guessed this letter"
                    print solution
                    letter = raw_input("Enter your next letter:").lower()
                if letter not in words[number]:
                    print "Wrong Guess!!You loose one chance"
                    chances -= 1
                    print "Your remaining chances are: "+str(chances)
                    print solution
                    letter = raw_input("Enter your next letter:").lower()

            elif len(letter) == 0:
                print "you did not enter anything"
                letter = raw_input("Enter your next letter:").lower()

            else:
                print "you entered more than 1 character"
                letter = raw_input("Enter your next letter:").lower()

        else:
                print solution
                print "Your chances are over You loose :("
                break





