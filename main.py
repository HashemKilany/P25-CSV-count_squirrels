import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#data.info()

black_count = len(data[data['Primary Fur Color'] == "Black"])
gray_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_count = len(data[data['Primary Fur Color'] == "Cinnamon"])

data_dic = {"fur_color": ["Black","Gray","Cinnamon"],
            "count": [black_count,gray_count,cinnamon_count]}
df = pandas.DataFrame(data_dic)
df.to_csv("squirrels_counts.csv")

