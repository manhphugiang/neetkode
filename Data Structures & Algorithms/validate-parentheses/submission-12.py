class Solution:
    def isValid(self, s: str) -> bool:
        s_list = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":
                s_list.append(char)
            else:
                if not s_list:
                    return False

                if s_list[-1] == pair[char]:
                    s_list.pop()
                else:
                    return False

        return len(s_list) == 0
