# Question 1
import pandas as pd
df = pd.read_csv('/depot/datamine/data/noaa/2020_sample.csv', names=["station_id", "date", "element_code", "value", "mflag", "qflag", "sflag", "obstime"])
df.head(10)
# The first 10 rows are provided. Obviously this is much easier than the for loop because this is only a one-line command, extremely easy to think about.


# Question 2
df.shape
print(f'There are {df.shape[1]} columns in the DataFrame!')
print(f'There are {df.shape[0]} rows in the DataFrame!')
# There are 8 columns and 15000000 rows in the dataframe.



# Question 3
my_dict = {"fruits": ["apple", "orange", "pear"], "person": "John", "vegetables": ["carrots", "peas"]}

# If "person" is indeed a key, they will function the same way
my_dict["person"]
my_dict.get("person")
my_dict.get("Same")
my_dict["Same"]
station_ids = df["station_id"].dropna().tolist()
my_dict = {}
Unique1 = list(set(station_ids))
for i in Unique1:
    my_dict[i] = 0
for j in station_ids:
    my_dict[j]+=1
print(my_dict['US1MANF0058'])
print(my_dict['USW00023081'])
print(my_dict['US10sali004'])
# "get" function and braskets normally works the same, but when searching for a non-exist key, brackets would show an error but get method won't. The dictionary my_dict is designed as above.


# Question 4
df_intruder = pd.read_csv('/depot/datamine/data/noaa/2020_sampleB.csv', names=["station_id", "date", "element_code", "value", "mflag", "qflag", "sflag", "obstime"])
intruder_ids = df_intruder["station_id"].dropna().tolist()
Unique2 = list(set(intruder_ids))
for i in Unique2:
    if i not in Unique1:
        print(i)
df_intruder[df_intruder["station_id"] == "USFAKEROW22" ]
# The intruder row is printed.


# Question 5
import matplotlib.pyplot as plt
plt.plot([1,2,3,5],[5,6,7,8])
plt.show()
plt.close()
new_dict = {}
q_flag = df["qflag"].dropna().tolist()
Unique3 = list(set(q_flag))
for i in Unique3:
    new_dict[i]=0
for j in q_flag:
    new_dict[j]+=1
import itertools
Sliced = dict(itertools.islice(new_dict.items(),20))
plt.bar(Sliced.keys(), Sliced.values()) 
plt.scatter(df["qflag"].dropna().head(n=100) ,df["value"].head(n=100)) # Check the relationship between qflag and value
# First, I used itertools to slice the dictonary, and created a new dictonary of qflag. Then I draw the first 20 qflags and see how many times they appear in the full data set respectively. Then, I draw a scatter plot between values and qflag.



