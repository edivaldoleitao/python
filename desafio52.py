x = int(input('digite um numero:'))
count = 0
for c in range(1, x + 1):
    if x % c == 0:
        count += 1
if count >= 3:
    print('{} não eh primo'.format(x))
else:
    print('{} é primo'.format(x))

