class Solution(object):
    INT_MAX = (2 ** 31) - 1
    INT_MIN = - (2 ** 31)
    sign_list = ['+', '-']
    digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def chk_valid(self, ch):
        return ch in self.sign_list or ch in self.digit_list

    def myAtoi(self, str):
        sum = 0
        sign = 1
        if str is None:
            return sum
        str = str.strip()

        if len(str) == 0:
            return sum
        if isinstance(str, list):
            str = str[0]
        i = 0
        if not self.chk_valid(str[i]):
            return 0

        while i < len(str):
            sum *= 10
            if i == 0 and str[i] in self.sign_list:
                sign = -1 if str[i] == '-' else 1
            elif str[i] not in self.digit_list:
                sum /= 10
                break
            else:
                sum += int(str[i])
            i += 1

        sum *= sign
        if sum > self.INT_MAX:
            sum = self.INT_MAX
        elif sum < self.INT_MIN:
            sum = self.INT_MIN
        return sum
