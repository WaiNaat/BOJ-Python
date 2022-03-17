# constant
C = 1000000000

# input
n = int(input())

# process
'''
F(n) = F(n-1) + F(n-2)   (n>1)
F(n) = F(n+2) - F(n+1)   (n<0)

음수 % c = c - (-음수 % c)로 나오므로 처리 필요
'''
F = [0, 1]

if n > 0:
    while len(F) < n + 1:
        F.append((F[-1] + F[-2]) % C)

elif n < 0:
    while len(F) < -n + 1:
        next = F[-2] - F[-1]
        sign = 1 if next > 0 else -1
        next = C - next % C if next < 0 else next % C
        F.append(sign * next)
    
# output
n = abs(n)
print(1 if F[n] > 0 else -1 if F[n] < 0 else 0)
print(abs(F[n]))