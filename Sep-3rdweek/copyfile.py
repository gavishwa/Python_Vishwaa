import shutil
def copyfile(srcf,dstf,n):
    fd=open(srcf,'r')
    fd1=open(dstf,'w')
    n=int(n)
    #lines =fd.readlines()
	#for line in lines:
	#    fd1.write(line)
    if int(n)==0:
        shutil.copyfileobj(fd,fd1)
    else:
        lines=fd.readlines()
        for line in lines:
            if int(n)!=0 and line !="":
                fd1.write(line)
                n-=1
    fd.close()
    fd1.close()
def main():
    srcf,dstf,n=eval(input("Enter the Source and Destination file Name and no of lines to copy:"))
    copyfile(srcf,dstf,n)
    
if __name__=='__main__':
    main()
