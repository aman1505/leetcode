from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result_set = []
        for email in emails :
            mid_index = email.find("@")
            domain = email[mid_index:]
            refined_local = email[0:mid_index].replace(".","")
            plus_index = refined_local.find("+")
            if plus_index == -1:
                refined_email = refined_local+domain
            else:
                refined_local = refined_local[0:plus_index]
                refined_email = refined_local+domain
            
            if refined_email not in result_set:
                result_set.append(refined_email)
        return (result_set)
            

if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    obj = Solution()
    result = obj.numUniqueEmails(emails)
    print(result)


        
        #     if plus_index != -1:                
        #         mid_index = refined_email.find("@")
        #         refined_email = refined_email[0:plus_index]+refined_email[mid_index:]
        #     if refined_email not in result_set:
        #         result_set.append(refined_email)
        # return len(result_set)