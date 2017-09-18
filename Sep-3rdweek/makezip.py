import sys
import shutil
import argparse
import os
def makezip(args):
#def makezip(a,b):
    bdir=args.i
    fname=args.d
    print("We are in makezip function")
    print(bdir,fname)
    zip_archive=shutil.make_archive(fname,"zip",bdir)
    #zip_archive=shutil.make_archive("a","zip","C:\\Users\\varunachalam\\Desktop\\Python_Class\\Scripts")
    #zip_archive.close()
    #print ("The ZIP  file created for folder",(bdir))
def main():
    print (sys.argv)
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",type=str,help="Input the Directory Path to add files into zip")
    parser.add_argument("-d",type=str,help="Input the ZIP File Name")
    args = parser.parse_args()
    print(args.i,args.d)
    makezip(args)
    #makezip("a","C:\\Users\\varunachalam\\Desktop\\Python_Class\\Scripts")
if __name__=="__main__":
    main()
    
    