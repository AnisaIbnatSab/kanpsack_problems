def knapsack(B, n, c, v):

    M = [[0 for _ in range(B + 1)] for _ in range(n + 1)]     # column and row M[i][w]
    C = [[False for _ in range(B + 1)] for _ in range(n + 1)]

    for b in range(B + 1):
        if v[0] <= b:
            M[1][b] = c[0]
            C[1][b] = True
        else:
            M[1][b] = 0
            C[1][b] = False

    for i in range(2, n + 1):
        for b in range(B + 1):
            if b >= v[i - 1] and M[i - 1][b - v[i - 1]] + c[i - 1] > M[i - 1][b]:
                M[i][b] = M[i - 1][b - v[i - 1]] + c[i - 1]
                C[i][b] = True
            else:
                M[i][b] = M[i - 1][b]
                C[i][b] = False

    included_items = []
    remaining_capacity = B
    for i in range(n, 0, -1):
        if C[i][remaining_capacity]:
            included_items.append(i)
            remaining_capacity -= v[i - 1]

    included_items.reverse()
    return M[n][B], included_items


# Input
n = int(input("Enter the number of items: "))
B = int(input("Enter the capacity of the knapsack: "))
c = []
v = []

print("Enter the cost and volume of each item:")
for i in range(n):
    cost = int(input(f"Cost of item {i + 1}: "))
    volume = int(input(f"Volume of item {i + 1}: "))
    c.append(cost)
    v.append(volume)


optimal_value, items_included = knapsack(B, n, c, v)


print(f"The optimal value is: {optimal_value}")
print(f"The items included in the knapsack are: {items_included}")