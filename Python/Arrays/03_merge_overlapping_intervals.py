'''
input:
6
22 28
1 8
25 27
14 19
27 30
5 12

output:
1 12
14 19
22 30
'''

class Pair:
    def __init__(self, st, et):
        self.st = st
        self.et = et

n = int(input())
pairs = []
for i in range(n):
    st, et = map(int, input().split())
    pairs.append(Pair(st, et))

pairs.sort(key=lambda x: x.st)

stack = []
for i in range(len(pairs)):
    if i == 0:
        stack.append(pairs[i])
    else:
        top = stack[-1]
        if top.et < pairs[i].st:
            stack.append(pairs[i])
        else:
            top.et = max(top.et, pairs[i].et)

for i in range(len(stack)):
    print(stack[i].st, stack[i].et)