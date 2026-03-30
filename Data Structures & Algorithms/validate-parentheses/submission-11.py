class Solution:
    def isValid(self, s: str) -> bool:
        s_list = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":
                s_list.append(char)
            else:
                # 🚨 missing guard
                if not s_list:
                    return False

                if s_list[-1] == pair[char]:
                    s_list.pop()
                else:
                    return False

        # 🚨 also missing final check
        return len(s_list) == 0
