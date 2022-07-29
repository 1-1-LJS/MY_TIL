# Input # of total cases
# Input # of data and data for each test case in 2 lines
# Input  first line - total case 't', second line - # of data, third line - data of test case
# Calculate the mean income and count # of households that earn less than a mean income.
# print out the order of test case and the result by '#? result' format



total = int(input()) # total cases
 
for testcase in range(1,total+1): # # of test case
    
    n = int(input()) # # of data
 
    income = list(map(int,input().split())) # Input data in int type
    
    mean_income = sum(income)/n     
    
    # count # of households earns less than mean income.
    cnt = 0
    
    for household in income:
        if household <= mean_income:
            cnt += 1
 
    print(f'#{testcase} {cnt}')