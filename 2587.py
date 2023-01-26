#대표값2
list=[]
for t in range(5):
    list.append(int(input()))
    
list = sorted(list)
print(int(sum(list)/5))
print(list[2])