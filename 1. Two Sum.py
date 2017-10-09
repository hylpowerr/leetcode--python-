class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
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