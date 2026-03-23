def max_dist_occur(a):
    res = 0
    for i in range(len(a) - 1):
        for j in range(i +1 , len(a)):
            if a[i]== a[j]:
                res = max(res,j - i)
    return res

if __name__ == "__main__":
    a = [1,3,3,1,66,7,2,3]
    print(max_dist_occur(a))
