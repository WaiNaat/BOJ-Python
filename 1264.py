import sys
input = sys.stdin.readline
import re

line = input().rstrip()
while line != '#':
	print(len(re.findall("[aeiouAEIOU]", line)))
	line = input().rstrip()