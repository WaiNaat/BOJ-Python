# function
def make_password(start_idx, L, C):
    '''letter[start_idx:]를 확인해서 암호를 만드는 함수'''
    # base case
    if len(password) == L:

        # 모음의 개수 세기
        vowel_cnt = 0
        for ch in password:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                vowel_cnt += 1
        
        # 자음의 개수 세기
        consonant_cnt = L - vowel_cnt

        # 조건에 맞으면 출력
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print("".join(password))
        
        return

    # recursive step
    for i in range(start_idx, C):
        password.append(letters[i])
        make_password(i + 1, L, C)
        password.pop()

# input
L, C = map(int, input().split())
letters = list(input().split())

# process
'''
최소 한 개의 모음, 두 개의 자음이 들어가야 함
itertools.permutation 돌리기에는 수가 너무 크다

글자들을 오름차순 정렬하고
조합할 때 다음 글자는 지금 글자 이후 글자들에서만 찾아서 진행
완성한 후에 모음이 있는지 확인하고 출력
'''
letters.sort()

password = []
make_password(0, L, C)