code13:
class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {"I":1, "V":5,"X":10, "L":50, "C":100,
         "D":500, "M":1000}
        romandict_div = {"IV":4 ,"IX": 9, "XL":40, "XC":90,
         "CD":400, "CM":900}
        total = 0
        for k in romandict_div.keys():
                if k in s:
                    total += romandict_div[k]
                    s = "".join(s.split(k))
        for m in s:
            if m in romandict:
                total += romandict[m]
        return total
        
        
code14:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        fir_str, length = strs[0], len(strs)
        for i in strs[1:]:
            fir_str = self.scp(fir_str, i)
            if not fir_str:
                break
        return fir_str
    
    def scp(self, str1, str2) -> str:
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
