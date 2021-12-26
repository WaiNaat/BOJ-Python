import re
# input
paragraph = input()
# process
'''
질문을 따로 분리.
답변 제작.
'''
result = re.findall("What is[a-z ,;'\-]*\?", paragraph)
result = [re.sub("What(?P<question>.*)\?", "Forty-two\g<question>.", s) for s in result]
# output
for answer in result: print(answer)