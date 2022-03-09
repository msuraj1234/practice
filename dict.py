str = 'aabbcd'
d = {}
for i in str:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        if d[i]>1:
            d.pop(i, None)
print(list(d.keys()))

            

        
    
