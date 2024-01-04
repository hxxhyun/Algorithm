# answer[i] : i번째 날 이후로 따뜻한 온도가 나타나기까지 기다려야하는 날짜 수(따뜻해지지 않으면 0)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex

            stack.append(i)
        
        return result