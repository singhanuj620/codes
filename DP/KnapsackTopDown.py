

wt = [10, 20, 30]
val = [60, 100, 120]
w = 50
# O/P = 220
n = len(wt)
lst = []
for i in range(n+1):
    for j in range(w+1):
        lst.append([-1]*(w+1))


for i in range(n+1):
    for j in range(w+1):
        if i == 0 or j == 0:
            lst[i][j] = 0
        else:
            if wt[i-1] <= j:
                lst[i][j] = max(val[i-1] + lst[i-1][j-wt[i-1]], lst[i-1][j])
            else:
                lst[i][j] = lst[i-1][j]

print(lst[n][w])
