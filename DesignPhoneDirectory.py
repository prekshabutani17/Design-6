"""
Time Complexity : O(1) for get(), check() and release() 
Space Complexity : O(maxNumbers)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
"""
from collections import deque
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.q = deque()
        self.hashSet = set()
        for i in range(maxNumbers):
            self.q.append(i)
            self.hashSet.add(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if len(self.q) == 0: return -1
        num = self.q.popleft()
        self.hashSet.remove(num)
        return num

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.hashSet

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.hashSet: return
        self.hashSet.add(number)
        self.q.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)