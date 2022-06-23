# n = int(input())

# for i in range(n):
# d,c = input().split(' ')
# d,c = int(d), int(c)

# items1 = input().split(' ')
# items1 = [int(x) for x in items1]

# items2 = input().split(' ')
# items2 = [int(x) for x in items2]

d,c = 90, 100
items1 = [100, 50, 10,]
items2 = [80, 80, 80]

tot1 = 0
for item in items1:
    tot1 += item
    
tot2 = 0
for item in items2:
    tot2 += item
    
    
del_cost_c = 0

if 150 >= tot1:
    del_cost_c += d 
if 150 >= tot2:
    del_cost_c += d
    
if c < del_cost_c:
    print('YES')
else:
    print('NO')
        
        
        
    