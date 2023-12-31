matrix = []

for i in range(5):
    lst = input().strip()
    lt = list(map(int, lst.split()))
    matrix.append(lt)

ans = 0 
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            ans = abs(2-i) + abs(2-j)
            break
print(ans)