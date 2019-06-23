def main():
  testcase1=["name, age, gender, year, comment", "Vincent, 23, male, sophomore, laji", 
  "Wolei, 24, femail, freshman, shabi langzi duodiao", 
  "   wolun, 26, male, junior,    fdsafljalkfdsa", 
  "shi zhen de qiang, 100, male, senior, the mysterious man"]

  lines=csv_format(testcase1)
  for line in lines:
    for col in line:
      print col, 
    print

def csv_format(arr):
  col_count=len(arr[0].split(","))
  col_len=[0]*col_count
  lines=[]
  for i in range(0, len(arr)):
    line=arr[i].split(",")
    for j in range(0, len(line)):
      col=line[j].strip()
      line[j]=col
      if len(col)>col_len[j]:
        col_len[j]=len(col)
    lines.append(line)
  print col_len
  for i in range(0, len(lines)):
    for j in range(0, len(col_len)): 
      lines[i][j]=lines[i][j].rjust(col_len[j])+" "
    print
  return lines

main()