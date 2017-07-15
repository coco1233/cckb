import random
dictionary = ("puma", "corner", "spot", "accumulate", "evidence", "print", "cling", "oblige", "convince", "hunt", "blackberry", "somehow", "disturb")
right = "Y"
print "Welcome to word guess!"
while right == "Y":
    word = random.choice(dictionary)
    score = 100
    correct = word
