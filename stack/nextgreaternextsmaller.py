def nextGreater(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]

        stack.append(arr[i])

    return nge


def nextSmaller(arr):
    n = len(arr)
    nse = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            nse[i] = stack[-1]

        stack.append(arr[i])

    return nse


def nextSmallerOfNextGreater(arr):
    nge = nextGreater(arr)
    nse = nextSmaller(arr)

    result = []

    for i in range(len(arr)):
        if nge[i] == -1:
            result.append(-1)
        else:
            # find index of nge value
            idx = arr.index(nge[i])
            result.append(nse[idx])

    return result


arr = [5, 1, 9, 2, 5, 1, 7]
print(nextSmallerOfNextGreater(arr))