from typing import List
class Solution():
    def groupAnagrams(self, strs:List[str])-> List[List[str]]:
        result = []
        sorted_map = {}
        anagram_list =[]
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in sorted_map.keys():
                sorted_map[sorted_s]=list()
            sorted_map[sorted_s].append(s)

        for key,value in sorted_map.items():
            result.append(value)
        print(sorted_map)
        return result 

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    obj = Solution()
    result = obj.groupAnagrams(strs)
    print(result)