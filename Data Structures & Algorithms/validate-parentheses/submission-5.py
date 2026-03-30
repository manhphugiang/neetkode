class Solution:
    def isValid(self, s: str) -> bool:
        prev_len = -1

        # keep removing pairs until no change
        while prev_len != len(s):
            prev_len = len(s)
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return s == ""

