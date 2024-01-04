from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # 큐의 front에 원소를 추가하기 위해 두 번째 큐에 모든 원소를 이동
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # 새로운 원소를 첫 번째 큐에 추가
        self.queue1.append(x)
        # 두 번째 큐에 있는 모든 원소를 다시 첫 번째 큐로 이동
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        # 첫 번째 큐에서 가장 앞에 있는 원소를 제거하고 반환
        return self.queue1.popleft()

    def top(self) -> int:
        # 첫 번째 큐에서 가장 앞에 있는 원소를 반환 (제거하지 않음)
        return self.queue1[0]

    def empty(self) -> bool:
        # 스택이 비어있는지 여부를 반환
        return not bool(self.queue1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
