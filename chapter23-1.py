import random
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    dice_total = random.randint(1, 12)
    totals[dice_total] += 1
for i in range (1, 13):
    print "total", i, "came up", totals[i], "times"
