'''
앞에서부터 읽으면 되고
만약 C, X, I를 만나면
뒤에거 하나도 더 읽어서 4, 9, 40, 90, 400, 900 처리.

로마자로 다시 바꿀 때는
천의 자리부터 바꾸면 됨.
'''
# functinos
def roman2int(val):
    roman_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                   'C': 100, 'D': 500, 'M': 1000}
    idx = 0
    ret = 0
    
    while idx < len(val):
        cur = val[idx]
        idx += 1

        if idx == len(val):
            ret += roman_table[cur]

        elif cur == 'C' and val[idx] == 'M':
            ret += 900
            idx += 1
        
        elif cur == 'C' and val[idx] == 'D':
            ret += 400
            idx += 1
        
        elif cur == 'X' and val[idx] == 'C':
            ret += 90
            idx += 1
        
        elif cur == 'X' and val[idx] == 'L':
            ret += 40
            idx += 1
        
        elif cur == 'I' and val[idx] == 'X':
            ret += 9
            idx += 1
        
        elif cur == 'I' and val[idx] == 'V':
            ret += 4
            idx += 1

        else:
            ret += roman_table[cur]
    
    return ret

def int2roman(val):
    ret = []

    while val >= 1000:
        ret.append('M')
        val -= 1000

    if val >= 900:
        ret.append("CM")
        val -= 900
    
    if val >= 500:
        ret.append('D')
        val -= 500

    if val >= 400:
        ret. append("CD")
        val -= 400
    
    while val >= 100:
        ret.append('C')
        val -= 100

    if val >= 90:
        ret.append("XC")
        val -= 90

    if val >= 50:
        ret.append('L')
        val -= 50
    
    if val >= 40:
        ret.append("XL")
        val -= 40

    while val >= 10:
        ret.append('X')
        val -= 10
    
    if val >= 9:
        ret.append("IX")
        val -= 9
    
    if val >= 5:
        ret.append('V')
        val -= 5
    
    if val >= 4:
        ret.append("IV")
        val -= 4

    while val > 0:
        ret.append("I")
        val -= 1

    return ''.join(ret)   


# input
val1 = input()
val2 = input()

# process
sum = roman2int(val1) + roman2int(val2)
sum_roman = int2roman(sum)

# output
print(sum)
print(sum_roman)