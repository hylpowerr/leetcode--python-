class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        url:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
        将str转换成list 便于定位下标以及判重
        """
        li = []
        for si in s:
            li.append(si)
        # print(li[1:-1])
        max_list = []
        tmp_list = []
        start_index = 0
        end_index = 0
        for index in range(len(li)):
            tmp_s = li[index]
            if not tmp_s in tmp_list:
                tmp_list.append(tmp_s)
                if len(tmp_list)> len(max_list):
                    max_list = tmp_list
            else:
                for ti in range(len(tmp_list)):
                    if tmp_list[ti] == tmp_s:
                        tmp_list = tmp_list[ti+1:]
                        tmp_list.append(tmp_s)
                        break
        # st =''
        # for each in max_list:
        #     st = st+each
        return len(max_list)




if __name__ == '__main__':
    ex = Solution()
    result = ex.lengthOfLongestSubstring("aab")
    print(result)