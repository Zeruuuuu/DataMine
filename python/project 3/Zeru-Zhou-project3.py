# Question 1
from block_timer.timer import Timer
import pandas as pd


Intruder = pd.read_csv('/depot/datamine/data/noaa/2020_sampleB.csv', names=["station_id", "date", "element_code", "value", "mflag", "qflag", "sflag", "obstime"])
intruder_ids = Intruder["station_id"].dropna().tolist()
unique_intruder = list(set(intruder_ids))


Original = pd.read_csv('/depot/datamine/data/noaa/2020_sample.csv', names=["station_id", "date", "element_code", "value", "mflag", "qflag", "sflag", "obstime"])
original_ids = Original["station_id"].dropna().tolist()
unique_ids = list(set(original_ids))

with Timer():
    # compare the two lists
    for i in unique_intruder:
        if i not in unique_ids:
            print(i)
with Timer():
    print(set(intruder_ids) - set(original_ids))
# As we can see, doing set calculation is much time efficient than checking with a loop. It is 22 times faster than the original method.



# Question 2
import pandas as pd

mydf = pd.read_csv("/depot/datamine/data/iowa_liquor_sales/clean_sample.csv", sep=";")
sales_list = mydf['Sale (Dollars)'].dropna().tolist()
from block_timer.timer import Timer
with Timer(title = "List Loop"):
    value = 0.0
    for i in sales_list:
        value += i
    print(f'Average Sales is {value/len(sales_list)}')
with Timer(title = "Series Loop"):
    value = 0.0
    for idx, val in mydf['Sale (Dollars)'].dropna().iteritems():
        value += val
    print(f'Average Sales is {value/len(sales_list)}')
# Method with list loop is 4 times faster than Series loop.




# Question 3
with Timer(title="Loops"):

    # calculate the mean
    mean = sum(sales_list)/len(sales_list)

    # calculate the std deviation
    # you can use **2 to square a value and
    # **0.5 to square root a value
    Std_sqr = 0
    for value in sales_list:
        Std_sqr += (value - mean)**2 / len(sales_list)
    My_std = Std_sqr ** 0.5

    # calculate the list of z-scores
    zscores = []
    for value in sales_list:
        zscores.append((value - mean) / My_std)
        

    # print the first 5 z-scores
    print(zscores[:5])
with Timer(title="Vectorization"):
    print(((mydf['Sale (Dollars)'] - mydf['Sale (Dollars)'].mean())/mydf['Sale (Dollars)'].std()).iloc[0:5])
# The results are exactly the same. Using Series is 5 times faster than using for loops here.



# Question 4
import pandas as pd
from collections import defaultdict
mydf = mydf.loc[:, ('Store Number', 'Volume Sold (Gallons)')]
volumn_dict = defaultdict(int)
for idx, val in mydf.iterrows():
    volumn_dict[val['Store Number']] += val['Volume Sold (Gallons)']
# The volumn dictionary is created with keys and values correspond to these 2 columns.



# Question 5
for key in volumn_dict:
    if volumn_dict[key] < 100000:
        continue
    elif volumn_dict[key] > 149999:
        print(f'High: {key}')
    else:
        print(f'Low: {key}')
# As code above, we got the output we want.


