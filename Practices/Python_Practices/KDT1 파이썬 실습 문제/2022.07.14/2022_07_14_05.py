word = input()

result = {}
for char in word:
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1
print(result)

result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
print(result)

for key in result:
    print(key, result[key])



# 18.알파벳 등장 갯수 구하기 - Alternative
# alpha={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
#        'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,
#        'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
# word=input().rstrip()

# for i in word:
#     alpha[i]+=1
# for k,v in alpha.items():
#     if v>=1:
#         print(k,v)