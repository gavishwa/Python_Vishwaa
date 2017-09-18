import sys
import shutil
import argparse

def copyfile2(args.i,args.d,args.n):
    fd=open(args.i,'r')
    fd1=open(args.d,'w')
    n=int(args.n)
    if n==0:
        shutil.copyfileobj(fd,fd1)
    lines=fd.readlines()
    for line in lines:
        if n!=0 and n!="":
            fd1.write(line)
            n-=1
    fd1.close()
    fd.close()
			
	
def main():
    print (sys.argv)
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str,help="Input the Source File")
    parser.add_argument("-d",type=str,help="Input the Destination File")
    parser.add_argument("-n",type=int,help="Input the No of lines")
    args = parser.parse_args()
    print(args.i,args.d,args.n)
    copyfile2(args.i,args.d,args.n)
if __name__=="__main__":
    main()
    
    