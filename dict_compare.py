def dict_compare(d1,d2):
    retval=True
    #verify d1 is dictionary
    #verify if valuelist is a container
    if type(d1)!=dict or type(d2)!=dict:
        retval=False
    elif len(d1)!= len(d2):
	    retval=False
    else:
        for key in d1:
            if key in d2 and d1[key]==d2[key]:
                continue
            retval=False
            break
        else:	
            return retval
    return retval
def main():
    d1={}
    d2={}
    d1=eval(input("Enter the First Dict"))
    d2=eval(input("Enter the second Dict"))
    res=dict_compare(d1,d2)
    print ("The Entered Two Dictionaries are same",(res))
if __name__=='__main__':
    main()