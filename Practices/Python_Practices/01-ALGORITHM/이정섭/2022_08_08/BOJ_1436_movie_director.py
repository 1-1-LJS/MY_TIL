n = int(input())
cnt = 0
triple_six = 666
while True:
    if '666' in str(triple_six):
        cnt += 1
    if cnt == n:
        print(triple_six)
        break
    triple_six += 1