class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        第一种解决思路:暴力解决 时间复杂度为 O(n^2)
        第二种解决思路:先排序,取头和尾相加,若大于target则尾-1,若小于target则头+1 其时间复杂度为O(nlogn)
        第三种解决思路:使用python的dict,其类似于其他语言的map,其时间复杂度为O(n)
        """
        dic = {}
        for i in range(len(nums)):
            if not nums[i] in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
        for i in range(len(nums)):
            ot = target - nums[i]
            if ot in dic:
                if i in dic[ot]  :
                    if len(dic[ot]) > 1:
                        return [i, dic[ot][1]]
                    else:
                        continue
                else:
                    return [i, dic[ot][0]]


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    ex = Solution()
    result = ex.twoSum(nums,target)
    print(result)