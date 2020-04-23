# 题目：分割数组的最大值
# 难度；中等
# 对应知识点：二分
# 题号：LEETCODE 410
# 题目链接： https://leetcode-cn.com/problems/split-array-largest-sum/
# 题目描述：
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。


from itertools import combinations
nums = [7,2,5,10,8]#[1,8]
m = 2

# 暴力求解
combi=combinations(range(1,len(nums)),m-1)
sums=[]
for c in combi:
    maxnum=0
    c = [0] + list(c) + [len(nums)]
    for index,a in enumerate(c):
        if index < len(c)-1:
            cutsum = sum(nums[c[index]:c[index+1]])
            if maxnum<cutsum: maxnum=cutsum
    sums.append(maxnum)
if sums:print(min(sums))

# 二分法
def get_min_max(nums,m):
    if len(nums)==1: return nums[0]
    left = max(nums)
    right = sum(nums)
    while(right - left>0):
        mid= (left + right)//2
        sums = 0
        result=[]
        for index,value in enumerate(nums):
            sums = sums + value
            if sums<= mid:  continue
            else: 
                result.append(index)
                sums = value if value <= mid else result.append(index+1)
        k = len(result)+1
        if k <=m: right = mid
        else: left = mid+1
    return right
print(get_min_max(nums,m))


