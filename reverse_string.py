class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        srt=""
        i=len(s)-1
        while(i>=0):
            srt+=s[i]
            i-=1  
        s=srt
        print(s)
        return s
ob=Solution()
ob.reverseString(["h","e","l","l","o"])  
print(ob)     