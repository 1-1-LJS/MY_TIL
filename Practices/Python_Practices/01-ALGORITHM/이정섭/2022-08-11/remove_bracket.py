from itertools import combinations
problem = list(input()) 
p, brk_idx = [],[] 
result=set() 
for i,v in enumerate(problem): 
    if v == '(':
        problem[i]=''
        p.append(i)
    if v == ')':
        problem[i]=''
        brk_idx.append([p.pop(),i])      
for i in range(len(brk_idx)): 
    for j in combinations(brk_idx,i):
        P=problem[:] 
        for s,e in j:
            P[s]='(';P[e]=')' 
        result.add(''.join(P))
print(*sorted(result),sep='\n') 