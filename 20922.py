'''
투 포인터

dict로 연속부분수열 내 숫자들의 개수를 센다.
오른쪽 포인터를 증가시키는데 이때 해당 숫자가 K개를 넘었을 경우
K개가 되도록 왼쪽 포인터도 증가시킴.
'''
import sys
input = sys.stdin.readline

# input
N, K = map(int, input().split())
a = tuple(map(int, input().split()))

# process
left = 0
right = 1
numbers = {a[0]: 1}
sol = 1

while right < N:
    
    if a[right] in numbers:
        numbers[a[right]] += 1
    else:
        numbers[a[right]] = 1

    while numbers[a[right]] > K and left < right:
        numbers[a[left]] -= 1
        left += 1
    
    sol = max(right - left + 1, sol)
    right += 1

# output
print(sol)