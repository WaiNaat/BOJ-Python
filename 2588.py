val1 = int(input())
val2 = int(input())

a, b = divmod(val2, 100)
b, c = divmod(b, 10)

a *= val1 
b *= val1
c *= val1

print(c, b, a, val1 * val2, sep='\n')