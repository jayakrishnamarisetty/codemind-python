r,c=map(int,input().split())
mat=[]
even=0
odd=0
for i in range(r):
    sub=list(map(int,input().split()))
    mat.append(sub)
for i in range(r):
    for j in mat[i]:
        if j%2==0:
            even+=j
        else:
            odd+=j
print(even,odd)