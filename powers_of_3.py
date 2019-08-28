def largestPower(N):
    k=0
    while pow(3,k)<N:
        k+=1
    return k-1