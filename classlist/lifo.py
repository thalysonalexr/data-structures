stack = []

for e in ['a', 'b', 'c', 'd', 'e']:
    stack.append(e)
    print(stack)

print('\n')

while stack != []:
    rem = stack.pop()
    print(stack, '[%s]' % rem)

input()