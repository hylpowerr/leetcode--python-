"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        map = {}
        map[1] = ['()']
        map[0] = ['']
        def dp(n):
            if n == 1:
                return map[1]
            if n == 0 :
                return map[0]
            if n in map.keys():
                return map[n]
            ret_se = []
            for i in range(2,n-1):
                se0 = dp(i)
                se1 = dp(n-i)
                for each0 in se0:
                    for each1 in se1:
                        ret_se.append(each0 + each1)


            for each in dp(n-1):
                ret_se.append('('+each+')')
                ret_se.append('()'+each)
                ret_se.append(each+"()")
            return set(ret_se)

        ret_list =list(dp(n))
        return ret_list

if __name__ == '__main__':
    so = Solution()
    l = so.generateParenthesis(4)
    print(l)
    print(len(l))

