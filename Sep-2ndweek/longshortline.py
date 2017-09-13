def longestline(filename):
    fd=open(filename,'r')
    large_line_len=0
    for line in fd:
        if len(line) > large_line_len:
            large_line_len = len(line)
            large_line = line
    return large_line
    fd.close()
def shortestline(filename):
    fd=open(filename,'r')
    small_line_len=1000
    for line in fd:
        if len(line) < small_line_len:
            small_line_len = len(line)
            small_line = line
    return small_line
    fd.close()
def main():
    filename=eval(input("Enter the file Name:"))
    lline=longestline(filename)
    sline=shortestline(filename)
    print ("Longest Line in the file:::: " , lline)
    print ("Shortest Line in the file::: " , sline)
	
if __name__=='__main__':
    main()
