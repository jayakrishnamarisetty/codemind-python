n=int(input())
m=[]
l=list(map(int,input().split()))
for i in range(n):
    # if(l[i]<0):
    #     l[i]=-1*l[i]
    k=len(str((l[i])))
    m.append(k)
k=max(m)
for i in range(len(m)):
    if(m[i]==k):
        print(l[i],end=' ')
    