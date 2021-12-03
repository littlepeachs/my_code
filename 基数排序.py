def bucket_sort(A,base):
    buckets = [[] for _ in range(base)]#构建若干个桶
    for x in A:
        buckets[x.key()].append(x)#把元素加到桶中
    sorted_arr = []
    for bucket in buckets:
        sorted_arr+=bucket#直接合并列表
    return sorted_arr

def radix_sort(A,n_digits,base,max_len):
    B = [ myint(x,base=base,max_len = max_len) for x in A]
    result = []
    temp = B
    for j in range(n_digits):
        for x in B:
            x.undatekeydigit(j)
        temp= bucket_sort(temp,base)
    result = [x.value for x in temp]
    return result

def getdigit(x,base,max_len):#base是基底，在base进制下做基数排序
    digits = []
    while x>0:
        digits.append(x%base)
        x = x//10
    while(len(digits)<max_len):
        digits.append(0)
    return digits

class myint:
    def __init__(self,x,base,max_len,keydigit = 0):
        self.digits = getdigit(x,base,max_len)
        self.keydigit = keydigit
        self.value = x
    def key(self):
        if len(self.digits)>self.keydigit:
            return self.digits[self.keydigit]
    def undatekeydigit(self,p):
        self.keydigit = p
    def getvalue(self):
        return self.value
count1,count2 = 0,0
arr = [123,4,14,10009,654]
max_elem = max(arr)
min_elem = abs(min(arr))
max_len = 0
while(max_elem>0):
    max_elem//=10
    count1+=1
while(min_elem>0):
    min_elem//=10
    count2+=1
if(count2<count1):max_len = count1
else:max_len = count2
arr =radix_sort(arr,max_len,10,max_len)
print(arr)
