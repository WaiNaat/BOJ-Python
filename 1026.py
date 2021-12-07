# input
N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# process
# 어차피 S값 구하는거라 B 재배열 금지 조건은 무시 가능
# 큰거는 작은거랑, 작은거는 큰거랑 곱하면 된다.
A.sort()
B.sort(reverse=True)
S = sum(A[i] * B[i] for i in range(N))

# output
print(S)