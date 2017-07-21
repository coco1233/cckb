number = int(raw_input("Which multiplication table would your like?:"))
print "Here's your table:"
for looper in range(1, 11):
    print number, '\t*', looper, '\t=', looper * number, '\t'
