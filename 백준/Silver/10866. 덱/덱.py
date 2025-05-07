import collections

deque = collections.deque()

N = int(input())
res = []

for _ in range(N):
  line = list(input().split())
  command = line[0]
  val = 0
  if len(line) > 1:
    val = int(line[1])

 

  if command == 'push_back' :
    deque.append(val)
  
  elif command == 'push_front' :
    deque.appendleft(val)
  
  elif command == 'pop_front' :
    if deque:
      res.append(deque.popleft())
    else :
      res.append(-1)
  
  elif command =='pop_back':
    if deque:
      res.append(deque.pop())
    else:
      res.append(-1)
  
  elif command == 'size':
    res.append(len(deque))
  
  elif command == 'empty':
    if deque:
      res.append(0)
    else :
      res.append(1)
  
  elif command =='front':
    if deque:
      res.append(deque[0])
      
    else :
      res.append(-1)
  
  elif command == 'back':
    if deque:
      res.append(deque[-1])   
      
    else :
      res.append(-1)



print('\n'.join(map(str, res)))
    