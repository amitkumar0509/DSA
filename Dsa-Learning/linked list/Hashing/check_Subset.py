def subset(a,b):
    m , n = len(a), len(b)
    for i in range(n):
        find = False
        for j in range(m):
            if b[i]==a[j]:
                find = True
                a[j] = -1 #mark as visited
                break
        if not find:
            return False
    else:
        return True
if __name__== "__main__":
    a = [11,3,44,232,424]
    b= [3]
    if subset(a,b):
        print("true")
    else:
        print("False")