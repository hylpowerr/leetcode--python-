"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def __init__(self):
        self.digit_map ={}
        self.digit_map['2'] = ['a','b','c']
        self.digit_map['3'] = ['d','e','f']
        self.digit_map['4'] = ['g','h','i']
        self.digit_map['5'] = ['j','k','l']
        self.digit_map['6'] = ['m','n','o']
        self.digit_map['7'] = ['p','q','r','s']
        self.digit_map['8'] = ['t','u','v']
        self.digit_map['9'] = ['w','x','y','z']


        self.last_lists =[]
        self.num = 0
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        self.dfs(digits,0,'')
        return self.last_lists


    def dfs(self,digits,i,tmp_str):
        if i == len(digits)-1:
            num_char = digits[i]
            for each_char in self.digit_map[num_char]:
                self.last_lists.append(tmp_str+each_char)
            return
        num_char = digits[i]
        for each_char in self.digit_map[num_char]:
            self.dfs(digits,i+1,tmp_str+each_char)



if __name__ == '__main__':
    so = Solution()
    so.letterCombinations('2')
    print(so.last_lists)

