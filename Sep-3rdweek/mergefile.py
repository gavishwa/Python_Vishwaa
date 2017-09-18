import sys
import shutil
import argparse
def mergefile(args):
    fd=open(args.i,'r')
    fd1=open(args.d,'r')
    fd2=open(args.o,'a')
    line_fd=fd.readlines()
    line_fd1=fd1.readlines()
    for line in line_fd:
        fd2.write(line)
        fd2.write("\n")
    for line1 in line_fd1:
        fd2.write(line1)
    fd.close()
    fd1.close()
    fd2.close()	

def main():
    print (sys.argv)
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str,help="Input the First File Name")
    parser.add_argument("-d",type=str,help="Input the Second File Name")
    parser.add_argument("-o",type=str,help="Input the Output File Name")
    args = parser.parse_args()
    print(args.i,args.d,args.o)
    mergefile(args)
	#print("The Given files are identical",
if __name__=="__main__":
    main()
    
    