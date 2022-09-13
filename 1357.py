X, Y = input().split()
REV = lambda x: int(str(x)[::-1])
print(REV(REV(X) + REV(Y)))