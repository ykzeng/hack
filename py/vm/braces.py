def braces(values):
	for val in values:
		print single_exp(val)

def single_exp(exp):
	brace_set=["{", "}", "[", "]", "(", ")"]
	stack=[]
	for val in exp:
		if val not in brace_set:
			return "NO"
		stack.append(val)
		if len(stack)>1 and is_pair(stack[len(stack)-2], stack[len(stack)-1]):
			stack=stack[:(len(stack)-2)]
	if len(stack)==0:
		return "YES"
	else:
		return "NO"

def is_pair(brace1, brace2):
	if (brace1=="{" and brace2=="}") or (brace1=="[" and brace2=="]") or (brace1=="(" and brace2==")"):
		return True


values=["{}[]()", "{[}]}", "{[]}"]
print single_exp(values[2])
