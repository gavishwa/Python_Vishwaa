
no =int(input("Enter your no"))
is_prime = True
for i in range(2,no):
    if no % i  == 0:
        is_prime = False
if is_prime ==True:
    print "%d is a prime number!" %no
else:
    print "%d is NOT a prime number!" % no


