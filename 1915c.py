import math
testcase = int(input().strip())

for i in range(0, testcase):
    n = int(input().strip())
    
    lst = input().strip()
    lt = list(map(int, lst.split()))
    summ = sum(lt)
    sqrtsum = int(math.sqrt(summ))
    if sqrtsum*sqrtsum == summ:
        print("YES\n")
    else:
        print("NO\n")
        