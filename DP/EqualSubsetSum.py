wt = [1, 1, 2, 1, 3]
# OP = True

n = len(wt)
lst = []
# t[n+1][sm+1]
sm = 0
for i in range(n):
    sm += wt[i]
if sm % 2 != 0:
    print("False")
else:
    sm = sm//2
    for i in range(n+1):
        for j in range(sm+1):
            lst.append([False]*(sm+1))
    for i in range(n+1):
        for j in range(sm+1):
            if i == 0 and j == 0:
                lst[i][j] = True
            else:
                if i == 0:
                    lst[i][j] = False
                elif j == 0:
                    lst[i][j] = True
                elif wt[i-1] <= j:
                    lst[i][j] = lst[i-1][j-wt[i-1]] or lst[i-1][j]
                else:
                    lst[i][j] = lst[i-1][j]
    print(lst[n][sm])
