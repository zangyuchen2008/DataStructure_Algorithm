# 题目：搜索插入位置
# 难度；简单
# 对应知识点：二分
# 题号：LEETCODE 35
# 题目链接： https://leetcode-cn.com/problems/search-insert-position/
# 题目描述：
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
nums = [1,3,4,5,9,10]
v = 6

# 谓词是大于等于，返回的是右区间对应的索引
def bia_div(nums, value):
    left = -1
    right =len(nums)-1
    while(right-left>1):
        mid = (right + left)//2
        if nums[mid] >= value: right = mid 
        else: left =mid
    return right
print(bia_div(nums,9))

# https://www.zhihu.com/question/36132386 豆瓣高赞回答
def lower_bound(array, first, last, value ):
    while first< last:
        mid = first + (last - first) //2
        if array[mid] < value: first = mid +1
        else: last = mid
    return first
print(lower_bound([1,3,5,2,8,5],0,5,5))