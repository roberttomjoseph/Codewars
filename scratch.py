passw = input()

if len(passw) >= 8 and len(passw) <=32:
    if passw[0] >= 'a' and passw[0] <= 'z':
        if passw[0] >= 'A' and passw[0] <= 'Z':
            if passw.isalpha():
                print('True')
else:
    print('False')