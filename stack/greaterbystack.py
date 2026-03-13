def greaternumbers(arr):
    stack = []
    result = []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(arr[i])

    return result[::-1]
if __name__ == "__main__":
    arr = [1, 5, 0, 3, 4, 5]
    ans = greaternumbers(arr)

    for x in ans:
        print(x, end=" ")