n=int(input())
lst=list(map(int,input().split()))
lst.reverse()
for i in lst:
    if i%2==0:
        print (abs(lst.index(i)-(n-1)))
        break