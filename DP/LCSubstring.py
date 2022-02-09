str1 = 'abcdxyz'
str2 = 'xyzabcd'
# op = 3 i.e anu

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
            t[i][j] = 0
mx = 0
for i in range(n+1):
    for j in range(m+1):
        if t[i][j] > mx:
            mx = t[i][j]
print(mx)
