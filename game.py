import random
dictionary = ("puma", "corner", "spot", "accumulate", "evidence", "print", "cling", "oblige", "convince", "hunt", "blackberry", "somehow", "disturb, manual, collar, sacrifice, privilege, dustman, corporation, overalls, shower, secret, status")
list1 = []
slot = []
wrongs = []
health = 10
word = random.choice(dictionary)
for x in word:
    list1.append(x)
    slot.append("_")
print "       WELCOME TO GAME      "
print slot
while 1:
    guess = raw_input("Enter your guess:")
    while guess in slot or guess in wrongs:
        guess = raw_input("input your guess:")
    if guess in list1:
        for n in range(0, 5):
            if guess in list1:
                slot[list1.index(guess)] = guess
                list1[list1.index(guess)] = '_'
    else:
        print "NOPE"
        wrongs.append(guess)
        print "Incorrec guesses:", wrongs
        health = health -1
        print "health: "+ "+" * health
        print slot
        if '_' in slot:
            pass
        else:
            print "You got it!"
            exit()
            if health == 0:
                print "Game over!"
                print "The word is"+ word
                exit()
