class Solution():
    def checkSquare(self, block: str)-> bool:
        x_coridinate = ord(block[0])
        y_coridibate = int(block[1])

        if (x_coridinate%2 ==0 and y_coridibate%2 ==0) or (x_coridinate%2 ==1 and y_coridibate%2 ==1):
            return False
        else:
            return True

if __name__ == "__main__":
    block = "c7"
    obj = Solution()
    result = obj.checkSquare(block)
    print(result)