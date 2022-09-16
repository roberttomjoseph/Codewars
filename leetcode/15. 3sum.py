import time
start_time = time.time()

def threeSum(nums):

    def len_fix(trip):
        if len(trip) == 2:
            if trip[0] + trip[0] + trip[1] == 0:
                trip.append(trip[0])
            elif trip[0] + trip[1] + trip[1] == 0:
                trip.append(trip[1])
        elif len(trip) == 1:
            trip.append(trip[0])
            trip.append(trip[0])
    
    poss = []

    for ii,i in enumerate(nums):
        for jj,j in enumerate(nums[ii:]):
            for kk,k in enumerate(nums[jj:]):
                if i + j + k == 0:
                    if ii != jj and jj != kk and ii != kk:
                        poss.append([i,j,k])

    dist = set()

    for triplet in poss:
            dist.add(frozenset(triplet))

    ans_list = []

    for frzset in dist:
        trip = list(frzset)
        len_fix(trip)
        ans_list.append(trip)


    return ans_list
nums = [9,-9,4,12,12,0,-14,-7,10,-1,11,-10,-3,2,-9,0,8,-9,-5,-1,10,5,13,-5,-9,-12,9,-3,10,10,-10,4,8,1,-7,-2,-14,-6,6,11,8,-6,9,13,11,7,-10,-4,14,0,3,1,-10,-7,3,-12,-3,-11,0,-8,-15,5,3,8,13,11,13,-15,-9,4,3,6,5,-11,-4,-6,4,1,5,-5,-13,-7,11,-8,2,-1,-12,14,3,3,13,-5,-14,-7,11,14,-11,9,6,-13,-9,-13,1,11,-9,12,-10,2,-1,3,12,-7,3,0,0,12,6,3,3,-13,14,1,-3]
threeSum(nums)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
