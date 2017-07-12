dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
    flag = raw_input("Add or look up a word?(a/1)")
    if flag == "a":
        word = raw_input("Type the word:")
        defintion = raw_input("Type the defintion:")
        dictionary[str(word)] = str(defintion)
         print "Word added!"
         pape = raw_input("Add or look up a word (a/1)?")
         if pape == 'a':
             print dictionary
         else:
             continue
    elif flag == 'c':
        check_word = raw_input("type the word:")
         for key in sorted(dictionary.keys()):
             if str(check_word) == key:
                 print "existence", key, dictionary[key]
                 break
             else:
                 off = 'b'
         if off == 'b':
             print "That word isn't in the dictionary yet."
         else:
             print "error type"
             break
