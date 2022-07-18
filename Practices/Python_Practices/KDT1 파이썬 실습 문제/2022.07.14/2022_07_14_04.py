s = input()
result = 0
for i in s:
    print(chr(ord(i)-32),end='')


# 17.소문자-대문자 변환하기(양방향)
# word=input().rstrip()

# for i in word:
#     k=ord(i)
#     if 65<=k<97:
#         print(chr(k+32),end="")
#     elif 97<=k<129:
#         print(chr(k-32),end="")


# 17.소문자->대문자로
# word=input().rstrip()

# for i in word:
#     k=ord(i)
    # if 65<=k<97:
    #     print(chr(k+32),end="")
    # if 97<=k<129:
    #     print(chr(k-32),end="")