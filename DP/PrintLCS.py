str1 = 'anuj'
str2 = 'abcuj'
# op = auj

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
s = ""
i = n
j = m
while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        s += str1[i-1]
        i -= 1
        j -= 1
    elif t[i-1][j] > t[i][j-1]:
        i -= 1
    else:
        j -= 1
print(s[::-1])
