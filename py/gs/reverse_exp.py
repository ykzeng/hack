def reverse(expression):
    """
    OA
    Reverse Algebraic Expression
    "-1.5*-2+-9--23"=>"-23--9+-2*-1.5"
    """
    ops=["+","-","*","/"]
    i=len(expression)-1
    num_start=i+1
    num=""
    new_exp=""
    while(i>=0):
        if expression[i] in ops:
            num=expression[(i+1):num_start]
            # failed #4,7 trying to find if I ignored negative numbers
            if expression[i-1] in ops or i-1<0:
                num=expression[i]+num
                new_exp+=num
            else:
                new_exp+=num+expression[i]
            num_start=i
        i-=1
    return new_exp+expression[0:num_start]
test1="-1*-2+-9--23"
print reverse(test1)