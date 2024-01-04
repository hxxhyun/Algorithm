class MyQueue:

    def __init__(self):
        # 두 개의 스택을 초기화합니다.
        self.stack1 = []  # enqueue용 스택
        self.stack2 = []  # dequeue용 스택

    def push(self, x: int) -> None:
        # push 연산은 enqueue 연산이므로 stack1에 직접 요소를 추가합니다.
        self.stack1.append(x)

    def pop(self) -> int:
        # pop 연산은 dequeue 연산이므로 두 스택을 관리하여 구현합니다.

        # 만약 stack2가 비어있다면, stack1에서 모든 요소를 pop하여 stack2에 넣어줍니다.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # 이제 stack2에서 pop을 하면 가장 먼저 들어간 요소가 나옵니다.
        return self.stack2.pop()

    def peek(self) -> int:
        # peek 연산은 dequeue 연산과 비슷하게 구현하지만, 요소를 제거하지는 않습니다.
        # pop 연산과 동일한 방법으로 동작하되, stack2의 가장 위의 요소를 반환합니다.

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        # 양쪽 스택이 모두 비어있으면 큐는 비어있는 상태입니다.
        return not self.stack1 and not self.stack2
