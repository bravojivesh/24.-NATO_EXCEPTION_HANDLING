import pandas

dict={"Student": ["Angela", "Jivesh", "Harry"],"Score": [80,70,50]}
# print (dict)

df1=pandas.DataFrame(dict)
print (df1)

df1_iterrow=df1.iterrows()
# print (df1_iterrow)

for index,row in df1_iterrow:
    print (row, end="\n\n")
    print (row.Student, end= "\n*****\n")
    if row.Student=="Jivesh":
        print (f"here is the dishwasher: {row.Student} and his score is: {row.Score}")


