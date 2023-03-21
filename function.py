def counting():
    a=str(input('enter the name of the file '))
    w=0
    file=open(a,"r")
    for line in file:
        word=line.split()
        w=w+len(word)
    print(w)
counting()    