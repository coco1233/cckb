age = int(input())
if age > 0 and age < 17:
    print "Too young to vote"
elif age > 18:
    print "You can vote!"
else:
    print "You are a time traveller"
