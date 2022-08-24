words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

vertical = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            vertical += words[j][i]

print(vertical)