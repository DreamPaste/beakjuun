s = input()
result = []
for i in range(97, 123):
    result.append(s.count(chr(i)))
print(" ".join(map(str, result)))