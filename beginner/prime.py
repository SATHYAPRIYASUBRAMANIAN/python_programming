num=int(input("enter the number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"it is not a prime number")
        else:
            print(num,"is a prime number")
