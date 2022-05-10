input()
arr = input().split(' ')
arr_int = [int(x) for x in arr]
even_count = 0
for i in arr_int:
    if i % 2 == 0:
        even_count += 1

if even_count > len(arr) / 2:
    print('READY FOR BATTLE')
else:
    print('NOT READY')