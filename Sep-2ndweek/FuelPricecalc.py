#import sys
def FuelPricecalc(filename):
    fd=open(filename,'r')
    fd.seek(0)
    MH=0
    GA=0
    KA=0
    lineno=0
    for line in fd:
        wordslist=line.split()
        MH+=int(wordslist[2])
        GA+=int(wordslist[3])
        KA+=int(wordslist[4])
        lineno+=1
    fd.close()
    f=open("output.txt",'w')
    print ("AVG Fuel Price for the Year 2015 at MH" "GA" "KA", (MH/lineno,GA/lineno,KA/lineno),file=f)
    #f=open("output.txt",'w')
    #sys.stdout=f
	#f.write(print ("AVG Fuel Price for the Year 2015 at MH" "GA" "KA", (MH/lineno,GA/lineno,KA/lineno)))
    #print ("AVG Fuel Price for the Year 2015 at MH" "GA" "KA", (MH/lineno,GA/lineno,KA/lineno))
    f.close()
def main():
    filename=eval(input("Enter the file Name:"))
    FuelPricecalc(filename)
    
if __name__=='__main__':
    main()
