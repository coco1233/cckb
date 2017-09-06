timbitsleft = int(input("Enter purchase quantity:"))
totalcost = 0
if timbitsleft < 10:
    print timbitsleft * 0.2
elif timbitsleft >= 10 and timbitsleft < 20:
    print timbitsleft - 10 * 0.2 + 1.99
elif timbitsleft >= 20 and timbitsleft < 30:
    print timbitsleft - 20 * 0.2 + 3.39
elif timbitsleft >= 30 and timbitsleft < 40:
    print timbitsleft - 30 * 0.2 + 3.99 + 1.99
elif timbitsleft >= 40 and timbitsleft < 50:
    print timbitsleft - 40 * 0.2 + 6.19
elif timbitsleft >= 50 and timbitsleft < 60:
    print timbitsleft - 50 * 0.2 + 6.19 + 1.99
elif totalcost >= 60 and timbitsleft < 70:
    print timbitsleft - 60 * 0.2 + 6.19 + 3.39
else:
    bigboxes = int(timbitsleft / 40)
    totalcost = totalcost + timbitsleft * 6.19
    timbitsleft = timbitsleft - 40 * bigboxes
    totalcost = totalcost + timbitsleft
    print totalcost
