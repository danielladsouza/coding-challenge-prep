"""
    Implement a stack that supports push() pop() and peek() operations
"""
from typing import List

class Stack:
    def __init__(self):
        self._elements = []


    def push(self, value: int) -> None:
        self._elements.append(value)

    def pop(self) -> int:
        try:
            value = self._elements.pop()
            return value
        except IndexError as e:
            print("Stack is empty")

    def peek(self) -> int:
        try:
            value = self._elements[-1]
            return value
        except IndexError as e:
            print("Stack is empty")

    def empty(self) -> bool:
        return len(self._elements) == 0




