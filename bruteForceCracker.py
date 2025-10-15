plist = []
guessPassWd = "%(FGn"
# five character password
for a in range(40, 127):

    for b in range(40, 127):

        for c in range(40, 127):

            for d in range(40, 127):

                for e in range(40, 127):

                    valPassword = (chr(a) + chr(b) + chr(c) + chr(d) + chr(e))
                    print(valPassword)
                    plist.append(valPassword)
print(plist)

for item in plist:
    
    if (item == guessPassWd):
        print('Found password!')
        break

                    
    
