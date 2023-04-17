r,c=map(int,input().split())
mat=[]
s=0
s1=0
for i in range(r):
    sub_list = list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    if i%2==0:
        for j in mat[i]:
            s+=j
    else:
        for j in mat[i]:
            s1+=j
        
print(s,s1)