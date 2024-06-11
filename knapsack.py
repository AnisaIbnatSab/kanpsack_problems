def fractionalKnapsack(S, W):
    n = len(S)

    # item and weight
    xi = [0] * n
    vi = [0] * n

    # vi for each item
    for i in range(n):
        bi, wi = S[i]
        vi[i] = bi / wi

    w = 0
    max_benefit = 0

    while w < W:
        # highest value
        max_index = -1
        max_value = 0
        for i in range(n):
            if vi[i] > max_value:
                max_value = vi[i]
                max_index = i

        if max_index == -1:
            break

        # selected item
        bi, wi = S[max_index]
        amount = min(wi, W - w)

        # total weight and benefit
        w += amount
        max_benefit += amount * vi[max_index]
        xi[max_index] = amount

        # Remove
        vi[max_index] = 0

    # min
    w = 0
    min_benefit = 0

    while w < W:

        min_index = -1
        min_value = float('inf')
        for i in range(n):
            if vi[i] < min_value and vi[i] != 0:
                min_value = vi[i]
                min_index = i

        if min_index == -1:
            break

        # Determine the amount to take from the selected item
        bi, wi = S[min_index]
        amount = min(wi, W - w)

        # total weight and benefit
        w += amount
        min_benefit += amount * vi[min_index]

        # Remove
        vi[min_index] = float('inf')

    return xi, max_benefit, min_benefit


# Input
n = int(input("Enter the number of items: "))
W = int(input("Enter the maximum weight of the knapsack: "))
S = []

print("Enter the benefit and weight of each item:")
for i in range(n):
    bi = float(input(f"Benefit of item {i + 1}: "))
    wi = float(input(f"Weight of item {i + 1}: "))
    S.append((bi, wi))

result, max_benefit, min_benefit = fractionalKnapsack(S, W)

# Output the result
print("The amount of each item to take:")
for i in range(n):
    print(f"Item {i + 1}: {result[i]} units")

print(f"Maximum benefit: {max_benefit}")
print(f"Minimum benefit: {min_benefit}")


