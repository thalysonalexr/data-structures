deque = []

for e in ['d', 'e', 'f']:
    deque.append(e)
    print(deque)


for e in ['c', 'b', 'a']:
    deque.insert(0, e)
    print(deque)

print('\n')

for i in range(3):
    rem = deque.pop()
    print(deque, '[%s]' % rem)

for i in range(3):
    rem = deque.pop(0)
    print('[%s]' % rem, deque)

input()