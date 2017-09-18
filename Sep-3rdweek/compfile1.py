import sys
import shutil
import argparse
def compfile1(args):
    fd=open(args.i,'r')
    fd1=open(args.d,'r')
    line_fd=fd.readlines()
    line_fd1=fd.readlines()
    if line_fd==line_fd1:
        print ("The Given Files are Identical")
    else:
	    print ("The Given Files are NOT Identical")
	#return result

def main():
    print (sys.argv)
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str,help="Input the First File")
    parser.add_argument("-d",type=str,help="Input the Second File")
    args = parser.parse_args()
    print(args.i,args.d)
    compfile1(args)
	#print("The Given files are identical",
if __name__=="__main__":
    main()
    
    