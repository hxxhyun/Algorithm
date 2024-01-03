# 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in answer:
                answer[sorted_word].append(word)

            else:
                answer[sorted_word] = [word]

        result = list(answer.values())

        return result