num1=int(input("Enter the first number of the series "))
num2=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(num1,num2,end=" ")
while(n-2):
    c=num1+num2
    num1=num2
    num2=c
    print(c,end=" ")
    n=n-1
