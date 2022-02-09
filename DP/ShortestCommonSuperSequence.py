str1 = 'AGGTAB'
str2 = 'GXTXAYB'
# op = 9 i.e AGGXTXAYB
# m+n = worst case i.e longest supersequence
# i.e (m+n) - LCS
# LCS = GTAB coz that is common

n = len(str1)
m = len(str2)
t = [[0]*(m+1) for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            t[i][j] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            t[i][j] = 1 + t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j], t[i][j-1])
# Got length of LCS
print("length of LCS", t[n][m])
print(n+m-t[n][m])
