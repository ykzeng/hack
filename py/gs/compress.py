"""
OA
compress string
e.g.: ["a","a","b","b","c","c","c"]=>["a", "2", "b", "2", "c", "3", ...]
and return the length of compressed string
"""
def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i, j=0, 0
    while(i<len(chars)):
        char=chars[i]
        count=1
        k=i+1
        while(k<len(chars) and chars[k]==char):
            count+=1
            k+=1
        if count>1:
            count_str=str(count)
            for l in range(0, len(count_str)):
                chars[j+l+1]=count_str[l]
                print count_str[l]
            #chars[i+1]=str(count)
            chars[j]=char
            j+=len(count_str)+1
            i+=count
        else:
            chars[j]=char
            i+=1
            j+=1
    return j

test1=["a","a","b","b","c","c","c"]
print compress(test1)
print test1

test2=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print compress(test2)
print test2