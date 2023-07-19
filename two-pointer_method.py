n,m = 3,5
a = [2,8,8]
b = [3,4,5,5,10]
i = j = 0
c = []

while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
while j < m:
    c.append(b[j])
    j += 1  
while i < m:
    c.append(a[i])
    i += 1  

print(*c)