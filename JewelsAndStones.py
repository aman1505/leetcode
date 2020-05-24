class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0 
        for letter in S:
            print(letter)
            if letter in J:
                print("Yes")
                count = count + 1
        return count



if __name__ == "__main__":
    J = "z"
    S = "ZZ"
    obj = Solution()    
    result = obj.numJewelsInStones(J, S)
    print(result)
        