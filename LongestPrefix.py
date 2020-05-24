class Solution:
    def common_prefix(self, first, second):
        result = ""
        for i in range(len(first)+1):
            if first[0:i] == second[0:i]:
                result = first[0:i]
            else:
                break
        return result

    def longest_common_prefix(self,input_list):
        length = len(input_list)
        prefix = input_list[0]
        for i in range(length):
            prefix = self.common_prefix(prefix, input_list[i])
        return prefix

    def test(self,strs):
        if not strs:
            return ''
        strs.sort()
        print(strs)
        l = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < l and strs[0][i] == strs[-1][i]:
            i += 1
        return strs[0][:i]


if __name__ == "__main__":
    obj = Solution()
    inp = ["flower", "flo", "car", "fl"]
    res = obj.test(inp)
    print(res)