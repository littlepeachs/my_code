def bucket_sort(A,min_value,max_value):
    buckets = [[] for _ in range(min_value,max_value+1)]#构建若干个桶
    for x in A:
        buckets[x].append(x)#把元素加到桶中
    sorted_arr = []
    for bucket in buckets:
        sorted_arr+=bucket#直接合并列表
    return sorted_arr

arr = [5,1,7,6,8,9,3,2,0,18]
max = max(arr)
min = min(arr)
sorted_arr = bucket_sort(arr,min,max)
print(sorted_arr)
