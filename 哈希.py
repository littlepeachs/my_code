arr = [7,5,3,4,1,2,8]
buckets = [[] for i in range(5)]

def hash(x):
    return (x*7)%5

for i in range(len(arr)):
    buckets[hash(arr[i])].append(arr[i])

print(buckets)

buckets[hash(9)].append(9)
for i in range(len(buckets[hash(4)])):
    if buckets[hash(4)][i] == 4:
        del buckets[hash(4)][i]
        break
print(buckets)