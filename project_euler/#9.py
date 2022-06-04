# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

poss_a = [x for x in range(1,1001)]
poss_b = [x for x in range(1,1001)]
poss_c = [x for x in range(1,1001)]

triplet = []

for a in poss_a:
    for b in poss_b:
        c = (a**2 + b **2)**.5
        if int(c) == c and a + b + c == 1000:
            print(a*b*c)