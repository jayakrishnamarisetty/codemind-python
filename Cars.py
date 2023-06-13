def cars(n):
    if n/4==n//4:
        return(int(n/4))
    else:
        return((n//4)+1)
n=int(input())
print(cars(n))