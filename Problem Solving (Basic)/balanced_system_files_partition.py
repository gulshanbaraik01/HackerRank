def mostBalancedPartition(parent, files_size):
    n = len(parent)
    test_sum = [0 for i in range(n)]

    for i in range(0, n):
        temp = i
        while temp != -1:
            test_sum[temp] += files_size[i]
            temp = parent[temp]

    min_sum = abs(test_sum[0] - 2 * test_sum[1])
    for i in range(2, n):
        if min_sum > abs(test_sum[0] - 2 * test_sum[i]):
            min_sum = abs(test_sum[0] - 2 * test_sum[i])

    return min_sum

for _ in range(int(input())):
    parent = list(map(int, input().split(',')))
    files_size = list(map(int, input().split(',')))
    print(mostBalancedPartition(parent, files_size))
