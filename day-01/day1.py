input = open("input.txt", "r")
# input = open("test.txt", "r")

arr1, arr2 = [],[]

from collections import defaultdict
mp1, mp2 = defaultdict(int), defaultdict(int)

for row in input:
    v1, v2 = row.split()
    v1, v2 = int(v1), int(v2)
    arr1.append(v1)
    arr2.append(v2)
    mp1[v1]+=1
    mp2[v2]+=1

arr1.sort()
arr2.sort()
ans1 = 0
for v1,v2 in zip(arr1, arr2):
    ans1 += abs(v1-v2)
print(ans1)

ans2 = 0
for k,v in mp1.items():
    tmp = k*v*mp2.get(k, 0)
    ans2 += tmp
print(ans2)