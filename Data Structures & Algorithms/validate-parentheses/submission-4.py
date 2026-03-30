class Solution:
    def isValid(self, s: str) -> bool:
        s_list = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            # your idea: if it's an opening bracket, push to stack
            if char in "([{":
                s_list.append(char)
            else:
                # closing bracket: must have something to match
                if not s_list:
                    return False

                # your idea: check against the last opening bracket
                if s_list[-1] == pair[char]:
                    s_list.pop()          # consume the match
                else:
                    return False

        # valid only if no leftover opening brackets
        return len(s_list) == 0
