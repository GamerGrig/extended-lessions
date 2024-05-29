const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz'  # Строчные буквы

phrase = 'Day, mice. "Year" is a mistake!'

list_ = []
list_.extend(phrase.split())


result = ''

count_space = 0

for i in list_:
    count = 0
    for k in i:
        if k.isalpha():
            count += 1
    for j in i:
        if j.isupper():
            find_1 = const_upper.find(j)
            if (find_1 + count) >= len(const_upper):
                result += const_upper[(find_1 + count) - len(const_upper)]
            else:
                result += const_upper[find_1 + count]
            count_space += 1
        elif j.islower():
            find_2 = const_lower.find(j)
            if (find_2 + count) >= len(const_lower):
                result += const_lower[(find_2 + count) - len(const_lower)]
            else:
                result += const_lower[find_2 + count]
            count_space += 1
        elif j in [',', '.', '"', '!']:
            result += j
    if count == count_space:
        result += ' '
        count_space = 0


print(result)
