import sys

sys.stdin = open("_문자열의거울상.txt")

total = int(input())

# Use dictionary to define key and value for input
mirror = {
    'b':'d', 'd':'b', 'p':'q', 'q':'p' 
}
# when you use 'b:d', it will define b as d but d will be still d, so you have to identicate d as b

for i in range(1,total+1):
    words = list(input())

    for j in range(len(words)):
        words = mirror # Input of words need to change based on value in dictionary

    print(f'#{i} {words}')