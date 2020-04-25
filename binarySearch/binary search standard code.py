nums =[1,2,3,4,9,11]
target = 5

def bins_bigger_equal(nums,target):
    left = -1 #左边界为-1
    right = len(nums)#右边界比最大索引大1
    while right - left >1 :
        mid = left + (right -left) //2 #(right+left)//2也可以，此处方法不容易溢出，效果更好
        if nums[mid] >= target: right = mid #谓词大于等于
        else: left = mid 
    return right #返回右侧闭间

def bins_less(nums,target):
    left = -1 #左边界为-1
    right = len(nums) #右边界比最大索引大1
    while right - left >1 :
        mid = left + (right -left) //2 #(right+left)//2也可以，此处方法不容易溢出，效果更好
        if nums[mid] < target:left = mid  #谓词小于
        else: right = mid
    return right #返回右侧闭区间

print(bins_less(nums,target))
