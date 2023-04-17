r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in mat[i]:
        s+=j
print(s)
        