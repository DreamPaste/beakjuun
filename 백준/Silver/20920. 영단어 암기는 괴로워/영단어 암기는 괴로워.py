
import sys

n, m = map(int, sys.stdin.readline().split(' '))
note = dict() 
for i in range(n):
    word = sys.stdin.readline().strip()
    if(len(word)>=m) : # 길이가 m 이상인 단어들만 외웁니다.
        
        if word in note: # 단어가 존재한다면 단어에 카운트를 추가
            note[word][0] +=1
        else : 
            note[word] = [1, len(word), word]
ans = sorted(note.items(), key= lambda item:(-item[1][0], -item[1][1], item[1][2]))
for word in ans:
    print(word[0])

