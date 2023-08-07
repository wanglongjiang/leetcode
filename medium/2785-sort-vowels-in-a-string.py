class Solution:
    def sortVowels(self, s: str) -> str:
        vset = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels = [ch for ch in s if ch in vset]
        vowels.sort()
        ans = []
        i = 0
        for ch in s:
            if ch in vset:
                ans.append(vowels[i])
                i += 1
            else:
                ans.append(ch)
        return ''.join(ans)


s = Solution()
assert s.sortVowels('lEetcOde') == 'lEOtcede'
assert s.sortVowels('lYmpH') == 'lYmpH'
