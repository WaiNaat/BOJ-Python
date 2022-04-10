'''
4 7
47 74 44 77
474 744 444 774 477 747 447 777

4와 7로만 이루어진 x자리 수를 만드는 법:
    x-1 자리 수의 뒤에 4와 7을 붙인다.

이 원리를 이용해서 K번째 작은 수가 몇 자리인지,
그 자릿수에서 몇 번째 숫자인지 알 수 있음.

'몇 번째 숫자인지'를 이진수로 바꿔서
0을 4로, 1을 7로 치환한 후에
'몇 자리인지'가 되도록 앞에 4를 붙여주면 됨.
'''

# input
K = int(input())

# process
# K번째 작은 수가 몇 자리의 몇 번째 숫자인지 계산
cnt = 0
digit = 1
while cnt + 2 ** digit < K:
    cnt += 2 ** digit
    digit += 1

cnt = K - cnt - 1

# 해당 숫자 계산
cnt = bin(cnt)[2:]
sol = ['4'] * (digit - len(cnt))
for num in cnt:
    if num == '0':
        sol.append('4')
    else:
        sol.append('7')

# output
print(''.join(sol))