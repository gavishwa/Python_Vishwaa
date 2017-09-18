import sys
import shutil
import argparse
import filecmp
def compfile(args):
    #fd=open(args.i,'r')
    #fd1=open(args.d,'r')
    result=filecmp.cmp(args.i,args.d)
    if result==True:
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
    compfile(args)
	#print("The Given files are identical",
if __name__=="__main__":
    main()
    
    