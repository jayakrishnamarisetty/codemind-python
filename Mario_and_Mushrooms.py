def mario(a):
    if (a==0):
        return("NORMAL")
    elif(a==1):
        return("HUGE")
    elif(a==2):
        return("SMALL")
a=int(input())
a=a%3
print(mario(a))