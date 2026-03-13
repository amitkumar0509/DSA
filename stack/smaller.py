def prevSmaller(arr):
    n = len(arr)
    result = [-1] * n

    
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
    return result
    
if __name__ == "__main__":
    arr = [1, 5, 0, 3, 4, 5]
    ans = prevSmaller(arr)

    for x in ans:
        print(x, end=" ")