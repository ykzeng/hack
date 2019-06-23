"""
keng:
1. ascii code comparison, a-f/A-F instead of a-z/A-Z
2. leading zero validation
"""
class Solution(object):
	def validIPAddress(self, IP):
		"""
		:type IP: str
		:rtype: str
		"""
		if "." in IP:
			arr=IP.split(".")
			if len(arr)==4:
				for num in arr:
					if not self.is_sub_v4(num):
						return "Neither"
				return "IPv4"
		elif ":" in IP:
			arr=IP.split(":")
			if len(arr)==8:
				for num in arr:
					if not self.is_sub_v6(num):
						return "Neither"
				return "IPv6"
		return "Neither"
	
	def is_sub_v4(self, num):
		if (num.isdigit() and int(num)<256):
			if ("0" not in num) or (num.index("0")>0 or len(num)==1):
				return True
		return False
	
	def is_sub_v6(self, num):
		if len(num)<=4 and len(num)>0:
			for n in num:
				asc=ord(n)
				if (ord("f")>=asc>=ord("a")) or (ord("9")>=asc>=ord("0")) or (ord("F")>=asc>=ord("A")):
					continue
				else:
					return False
			return True
		return False

"""
sample solution from lc discussion
what to learn:
1. use set of characters at first to avoid complex ascii comparisons
"""
class Solution_sample(object):
    def validIPAddress(self, IP):
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
        ary = IP.split('.')
        if len(ary) == 4:
            for i in xrange(len(ary)):
                if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in xrange(len(ary)):
                tmp = ary[i]
                if len(tmp) == 0 or not len(tmp) <= 4 or not is_hex(tmp):    
                    return "Neither"
            return "IPv6"
        return "Neither"
		

sol=Solution()
ip="20EE:FGb8:85a3:0:0:8A2E:0370:7334"
ip="192.0.0.1"
print sol.validIPAddress(ip)