# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for txt in fh:
    txt = txt.rstrip()
    print(txt.upper())
