class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move_in_to_out()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move_in_to_out()
        return None if len(self.out_stack) == 0 else self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        self.move_in_to_out()
        return len(self.out_stack) == 0

    def move_in_to_out(self):
        if (len(self.out_stack) == 0):
            while (len(self.in_stack) > 0):
                self.out_stack.append(self.in_stack.pop())
