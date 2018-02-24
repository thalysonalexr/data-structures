row = []

for e in [1, 2, 3, 4, 5]:
    row.append(e)
    print(row)

print('\n')

while row != []:
    rem = row.pop(0)
    print('[%s]' % rem, row)

input()