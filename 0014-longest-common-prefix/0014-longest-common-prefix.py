class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""

        if not strs:
            return res

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return res

            res += ch

        return res
          

        