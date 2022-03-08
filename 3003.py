original = (1, 1, 2, 2, 2, 8)
found = tuple(map(int, input().split()))
sol = [original[i] - found[i] for i in range(6)]
print(*sol)