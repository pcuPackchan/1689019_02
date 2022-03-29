Fname = "Guestlist.txt"
accessMod = "r"
myFile = open(Fname, accessMod)
myFile.write("Hi there!\n")
myFile.write("잘지내?\n")
myFile.close()