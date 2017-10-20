class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str


        test url:https://leetcode.com/problems/longest-palindromic-substring/description/
        s1:转换后的字符串
        size :辅助数组size[i]表示以字符T[i]为中心的最长回文字串的最右字符到T[i]的长度

        使用Manacher算法

        """
        #以'#'进行构造奇串 以'@', '$'对首尾定义方式越界
        s1 = '@#'
        for ch in s:
            s1 = s1+ch+"#"
        s1 = s1+'$'
        print(s1)

        size = [0]*len(s1)
        biggest = 0 #最大回文子串长度
        mx = 0 #mx即为当前计算回文串最右边字符的最大值
        po = 0 # po是小于i的最大回文串的中心的下标,它的回文右边界下标就是mx
        x =1 #记录下标
        for i in range(1,len(s1)-1):
            if mx > i:
                if size[2*po-i] < mx-i: #分2种情况 一种size[j]<mx-i
                    size[i] = size[2*po-i]
                else:#一种 size[j]>=mx-i
                    size[i] = 1
                    while True:
                        if s1[i - size[i]] == s1[i + size[i]]:
                            size[i] = size[i] + 1
                        else:
                            break
            else:
                size[i] = 1
                while True:
                    if s1[i-size[i]] == s1[i+size[i]]:
                        size[i] = size[i]+1
                    else:
                        break
            if size[i]+i-1 > mx:# 若新计算的回文串右端点位置大于mx，要更新po和mx的值
                mx = size[i]+i-1
                po = i
            if biggest < size[i]: #更新最大子串,并记录下标
                biggest = size[i]
                x = i
            # biggest = max(biggest,size[i])
        tmp = s1[x-size[x]+1:x+size[x]]
        tmp = tmp.replace('#',"")

        return tmp #返回size[i]中的最大值-1即为原串的最长回文子串长度

if __name__ == '__main__':
    s = 'ccc'
    ex = Solution()
    result = ex.longestPalindrome(s)
    print(result)
    