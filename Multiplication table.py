a, b, c, d = map(int, input("Введите 4 числа до 10: ").split())

if (a, b, c, d < 10) or (a <= b) or (c <= d):
    print('', end='\t')
    for i in range(c, d+1):
        print(i,end='\t')
    print('')
    for k in range(a, b+1):
        print(k, end='\t')
        for j in range(c, d+1):
            print(j * k, end='\t')
        print('')

