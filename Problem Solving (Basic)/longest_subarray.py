def longestSubarray(arr):
    cur = arr[0]
    prev = None
    curCount = curPrevCount = maxx = 0

    for i in range(len(arr)):
        if arr[i] == cur:
            curCount += 1
            curPrevCount += 1
        elif arr[i] == prev:
            prev = cur
            cur = arr[i]
            curCount = 1
            curPrevCount += 1
        else:
            maxx = max(maxx, curPrevCount)
            if abs(arr[i] - cur) > 1:
                cur = arr[i]
                prev = None
                curCount = 1
                curPrevCount = 1
            else:
                prev = cur
                cur = arr[i]
                curPrevCount = curCount + 1
                curCount = 1

    maxx = max(maxx, curPrevCount)
    return maxx

for _ in range(int(input())):
    arr = list(map(int, input().split(',')))
    print(longestSubarray(arr))
    
