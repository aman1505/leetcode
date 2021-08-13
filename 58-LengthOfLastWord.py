class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trim_string = s.strip()
        split_string = trim_string.split()
        last_word = split_string[-1]
        return len(last_word)

if __name__ ==  "__main__":
    input = "   fly me   to   the moon  "
    obj = Solution()
    result = obj.lengthOfLastWord(input)
    print(result)
