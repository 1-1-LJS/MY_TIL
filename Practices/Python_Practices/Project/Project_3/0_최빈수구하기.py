
t = int(input()) # input # of test cases
n = int(input()) # Input the order # of test case
score_list = [] # make list for upcoming score input
for scores in range (1000): # 1000 scores
    score = map(int, input().split()) # acknowlege inputs as integer
    score_list.append(score)
    score_list.count(score)

print(t,f'#{n} {score}')