x=[]
n=int(input())
k=int(input())
'''
n=5
k=2
'''
sum=0
for i in range(n):
    x.append(int(input()))
for i in range(k):
    sum=sum+x[i]
print(sum)
