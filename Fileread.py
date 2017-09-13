def Fileread(f1):
    fh=open(f1)
    result= {}
    for line in fh:
        (key, value) = line.split(":"	)
        result[key]=value
    return result
def main():
    f1=eval(input("Enter the FileName"))
    res=Fileread(f1)
    print(res)
if __name__=='__main__':
    main()