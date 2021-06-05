class Solution():
    def sortSentence(self, s: str)-> str:
        result = ""
        list_of_words = s.split(" ")
        length_of_sentence = len(list_of_words)
        current_position = 0
        s_map = {}
        for word in list_of_words:
            desired_position = int(word[-1])
            s_map[desired_position]=current_position
            current_position+=1
        print(length_of_sentence)
        for pos in range(length_of_sentence):
            current_position = s_map[pos+1]
            word = list_of_words[current_position]
            word = word[0:-1]+" "
            result = result+word
        return result.strip(" ")

if __name__ == "__main__":
    str = "Myself2 Me1 I4 and3"
    obj = Solution()
    result = obj.sortSentence(str)
    print(result)
