import sys
input = sys.stdin.readline

def is_palindrome(s, erase_cnt):
    '''
    회문인지 검사하는 도중에 서로 다른 문자가 나왔다?
    그러면 왼쪽을 지웠을 때 유사회문인지 검사
    아니면 오른쪽을 지웠을 때 유사회문인지 검사
    '''
    if len(s) == 1:
        return erase_cnt

    left = 0
    right = len(s) - 1

    while left < len(s) // 2:
        
        if s[left] != s[right]:
            # 이미 한 번 지운 전적이 있으면 유사회문도 아님
            if erase_cnt == 1:
                return 2

            # 하나 지웠을 때 유사회문 가능성 보이면 지워봄
            ret = 2
            if s[left + 1] == s[right]:
                ret = min(ret, is_palindrome(s[left+1 : right+1], erase_cnt=1))
            if s[left] == s[right - 1]:
                ret = min(ret, is_palindrome(s[left : right], erase_cnt=1))
            return ret

        left += 1
        right -= 1
    
    return erase_cnt


T = int(input())
for _ in range(T):
    s = input().rstrip()
    print(is_palindrome(s, erase_cnt=0))