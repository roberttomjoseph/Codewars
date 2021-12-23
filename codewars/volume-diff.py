def volume_difference(a, b, c, d, e, f):
    if a*b*c >= d*e*f:
        return  a*b*c - d*e*f
    else:
        return d*e*f - a*b*c
    
print(volume_difference(1, 1, 1, 5, 5, 5))