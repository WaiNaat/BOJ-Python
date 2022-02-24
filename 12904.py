# input
s = list(input())
t = list(input())

# process
'''
t를 s로 바꾸는 걸 시도해본다.
t의 맨 뒤가 A면 A를 뺀다.
t의 맨 뒤가 B면 B를 빼고 뒤집는다.
>> 이렇게 반복해서 |s|=|t|가 됐는데 s!=t면 불가능.
'''
while len(s) != len(t):
	if t[-1] == 'A':
		t.pop()
	else:
		t.pop()
		t.reverse()

# output
print(1 if s == t else 0)