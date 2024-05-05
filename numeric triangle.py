currentNumber = 1
stop = 1
rows = int(input('Введите высоту треугольника: ')) + 1
for i in range(rows):
    for i in range(1, stop):
        print(currentNumber, end=' ')
        currentNumber += 1
    print("")
    stop += 1
