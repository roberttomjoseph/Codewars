def compare_triplets(a, b):
    alice = 0
    bob = 0
    for index, element in enumerate(a):
        if element > b[index]:
            alice += 1
        elif element < b[index]:
            bob += 1
        else:
            break
    return [alice, bob]