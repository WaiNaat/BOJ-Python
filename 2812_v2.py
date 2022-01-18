# input
n, k = map(int, input().split())
num = list(input())
# process
'''
i번째 숫자에 대해
	만약 내 앞의 숫자들이 나보다 작다면
	지울 수 있는 한도 내에서 앞의 숫자를 지움.
	나와 동등하거나 그 이상이면
	그 숫자는 살림. 
		>> 그 자리에 i번째 숫자가 들어가면 오히려 작아지기 때문
다 했는데 k개만큼 못 지웠으면 뒤에서부터 자른다.
'''
stack = []
for digit in num:
	while stack and k > 0 and stack[-1] < digit:
		stack.pop()
		k -= 1
	stack.append(digit)

for _ in range(k, 0, -1):
	stack.pop()
# output
print("".join(stack))