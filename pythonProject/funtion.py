def save_text(filename, text):
    fileobj = open(filename,"a")
    fileobj.write(text)
    return

filename = "1689019.txt"
text = input("Enter your text : ")
text = text + "\n"

save_text(filename,text)