'''
opt(i) := 2*i 크기의 직사각형 ... 방법의 수
opt(i) = opt(i-2) + opt(i-1)
    i-2에서 가로 2칸짜리 2개로 채우기
    i-1에서 세로 1칸짜리 1객로 채우기
'''
# input
n = int(input())

# process
opt = [1, 1]

for i in range(2, n + 1):
    opt.append((opt[i - 1] + opt[i - 2]) % 10007)

# output
print(opt[n])