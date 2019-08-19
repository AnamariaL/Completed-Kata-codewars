def get_middle(s): 
    i = int(len(s)/2)
    if len(s)%2==0:
        return s[i-1:i+1]
    else:
        return s[i:i+1]