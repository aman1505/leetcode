class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        result = -1
        if needle_length == 0:
            return 0
        for i in range(len(haystack)):                
            if needle == haystack[i:i+needle_length]:
                result=i
                break
        return result

if __name__ == "__main__":
    haystack= ""
    needle= "a"
    obj = Solution()
    result = obj.strStr(haystack,needle)
    print(result)

