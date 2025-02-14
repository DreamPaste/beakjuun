buggers =[]
sodas =[]
for i in range(5):
    if i <= 2:
        buggers.append(int(input()))
    else :
        sodas.append(int(input()))

print(min(buggers) + min(sodas) - 50)
