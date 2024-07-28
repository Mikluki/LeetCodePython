class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pali = None
        pali_len_max = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:  # EVEN CASE MET _I+1_ - MIDDLE
                pali_tmp = s[i] + s[i + 1]
                s_tmp = ""
                for k in range(1, n):
                    if i + 1 + k == n or i - k == -1:
                        break
                    if s[i - k] == s[i + 1 + k]:
                        s_tmp = s_tmp + s[i + 1 + k]
                    else:
                        break
                pali_len = len(s_tmp) * 2 + len(pali_tmp)
                print(pali_len)

                if pali_len > pali_len_max:
                    pali = s_tmp[::-1] + pali_tmp + s_tmp
                    pali_len_max = pali_len

            if i + 2 == n:
                break
            if s[i] == s[i + 2]:  # ODD CASE MET _I+1_ - MIDDLE
                pali_tmp = s[i] + s[i + 1] + s[i + 2]
                s_tmp = ""
                for j in range(1, n):
                    if i + 2 + j == n or i - j == -1:
                        break
                    if s[i - j] == s[i + 2 + j]:  # character from 2 to max
                        s_tmp = s_tmp + s[i + 2 + j]
                    else:
                        break

                pali_len = len(s_tmp) * 2 + len(pali_tmp)
                if pali_len > pali_len_max:
                    pali = s_tmp[::-1] + pali_tmp + s_tmp
                    pali_len_max = pali_len

        if pali is None:
            return s[0]
        return pali