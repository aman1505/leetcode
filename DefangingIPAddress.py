#1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address.replace(".","[.]")
        return address.replace(".","[.]")

if __name__ == '__main__':
    address = "1.1.1.1"
    obj = Solution()
    result = obj.defangIPaddr(address)
    print(result)