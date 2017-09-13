def linewordcharcount1(filename):
    fd=open(filename,'r')
    fd.seek(0)
    wc=0
    cc=0
    lc=0
    for line in fd:
        wordslist=line.split()
        lc+=1
        wc+=len(wordslist)
        cc+=len(line)
    print ("Total Lines " "Total Words " "Total CHARS ", (lc,wc,cc))
    fd.close()
def main():
    filename=eval(input("Enter the file Name:"))
    linewordcharcount1(filename)
    
if __name__=='__main__':
    main()
