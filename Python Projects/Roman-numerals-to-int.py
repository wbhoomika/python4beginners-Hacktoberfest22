class Solution:
    def romanToInt(s: str):
        list1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        p = 0
        for i in range(len(s)):
            if i+1 != len(s) and list1[s[i]] < list1[s[i+1]] :
                p = p - list1[s[i]]
            else:
                p = p + list1[s[i]]
        return p

    
s = str(input())
print(Solution.romanToInt(s)) 