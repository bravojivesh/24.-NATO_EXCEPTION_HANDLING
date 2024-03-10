import pandas
import pandas as pd

data1=pd.read_csv("nato_phonetic_alphabet.csv")
df1=pandas.DataFrame(data1)
df1_iter=df1.iterrows()

dict={row.letter:row.code for (ind,row) in df1_iter}

result_list=[]
def ask_f():
    global result_list
    ask = (input("Enter a name: ")).upper()
    result = []
    result = [dict[x] for x in ask]
    result_list=result

eog=False

while eog==False:
    try:
        ask_f()
    except KeyError:
        print ("Sorry must be characters")
    else:
        print(result_list)
        eog=True









