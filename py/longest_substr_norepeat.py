class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count=0
        if len(s)>0:
            max_count=1
        for sindex in range(len(s)):
            print "start from\t"+s[sindex]
            str_set={s[sindex]:1}
            count=1
            for eindex in range(sindex+1, len(s)):
                raw_input("getting to "+s[eindex])
                if s[eindex] not in str_set:
                    count+=1
                    str_set[s[eindex]]=1
                    print "get local longest: "+s[sindex:eindex]
                    if count>max_count:
                        print "identified as current global longest!"
                        max_count=count
                    sindex=eindex
                else:
                    break
        return max_count
                    
sol=Solution()
print sol.lengthOfLongestSubstring("au")