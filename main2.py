import pandas

data=pandas.read_csv("weather_data.csv")
data_to_df=pandas.DataFrame(data)
# print (data_to_df)

data_to_iter= data_to_df.iterrows()
# print (data_to_iter)

for (ind,row) in data_to_iter:
    if row.day=="Thursday":
        print(row.temp)

x= data[data.day=="Thursday"]
print (x.temp.item())