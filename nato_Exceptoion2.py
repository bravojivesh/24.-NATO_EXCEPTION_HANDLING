import pandas
import pandas as pd

data1=pd.read_csv("nato_phonetic_alphabet.csv")
df1=pandas.DataFrame(data1)
df1_iter=df1.iterrows()

dict={row.letter:row.code for (ind,row) in df1_iter}

def main_prog():
    try:
        ask = (input("Enter a name: ")).upper()
        result=[dict[x] for x in ask]
    except KeyError:
        print ("Sorry no numbers!!")
        main_prog()
    else:
        print(result)

main_prog()









