n=int(input("Enter the number"))
if n!=0:
    rem=n%10
    result=rem**3
    n=n/10
if result==n:
    print("it is an armstrong number")
else:
    print("It is not an armstrong number")
