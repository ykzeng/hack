
def to_bin(num):
	bin_str=""
	while (num>0):
		digit=num%2
		bin_str=str(digit)+bin_str
		num/=2
	return bin_str

test1=77
test2=164
test3=0
test4=1111
print "simple dec2bin: "+to_bin(test1)

def bin_analysis(num):
	length=0
	count=0
	arr=[]
	while (num>0):
		digit=num%2
		num=num/2
		if digit==1:
			count+=1
			arr=[length]+arr
		length+=1
	arr=[(length-1-i) for i in arr]
	arr=[count]+arr
	return arr

print "decimal "+str(test1)+" to [# of 1s, positions...]: "+str(bin_analysis(test1))
print "decimal "+str(test2)+" to [# of 1s, positions...]: "+str(bin_analysis(test2))
print "decimal "+str(test3)+" to [# of 1s, positions...]: "+str(bin_analysis(test3))