import pandas
import pandas as pd

data1=pd.read_csv("nato_phonetic_alphabet.csv")
df1=pandas.DataFrame(data1)
df1_iter=df1.iterrows()


dict={row.letter:row.code for (ind,row) in df1_iter}
# print(dict)

#JH: We have to use the above method, because the following does not work. It will create a dict
# in a different style. like this: {'letter': {0: 'A', 1: 'B', 2: 'C', 3....
# dict2=df1.to_dict()
# print (dict2)

# print (dict.keys())

ask=(input("Enter a name: ")).upper()
result=[]

# for letter in ask:
#     for key,val in dict.items():
#         if letter==key:
#             result.append(val)
# print (result)
#The above works, but I want to use list comprehension

# result=[dict[x] for x in ask if x in dict] #condition is not needed.
result=[dict[x] for x in ask]
print (result)

# result=[code for (letter,code) in dict.items() if letter in ask]
# result= [dict.values() for x in ask if x in dict.keys()]






