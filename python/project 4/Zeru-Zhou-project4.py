# Question 1
import pandas as pd
my_df = pd.read_csv("/depot/datamine/data/stackoverflow/unprocessed/2021.csv")
from block_timer.timer import Timer
with Timer(title="csv") as t1:
    my_df.to_csv("/scratch/brown/zhou902/2021.csv", index = False)
with Timer(title="parquet") as t2:
    my_df.to_parquet("/scratch/brown/zhou902/2021.parquet", index = False)
with Timer(title="feather") as t3:
    my_df.to_feather("/scratch/brown/zhou902/2021.feather")

print(t1.elapsed)
print(t2.elapsed)
print(t3.elapsed)
print(f'Parquet: {t2.elapsed/t1.elapsed:.1%}')
print(f'Feather: {t3.elapsed/t1.elapsed:.1%}')
with Timer(title="csv") as t1:
    pd.read_csv("/scratch/brown/zhou902/2021.csv")
with Timer(title="parquet") as t2:
    pd.read_parquet("/scratch/brown/zhou902/2021.parquet")
with Timer(title="feather") as t3:
    pd.read_feather("/scratch/brown/zhou902/2021.feather")

print(t1.elapsed)
print(t2.elapsed)
print(t3.elapsed)
print(f'Parquet: {t2.elapsed/t1.elapsed:.1%}')
print(f'Feather: {t3.elapsed/t1.elapsed:.1%}')
from pathlib import Path
print(f'csv: {Path("/scratch/brown/zhou902/2021.csv").stat().st_size/1000000}')
print(f'parquet: {Path("/scratch/brown/zhou902/2021.parquet").stat().st_size/1000000}')
print(f'feather: {Path("/scratch/brown/zhou902/2021.feather").stat().st_size/1000000}')
# In writting, parquet is 18.5% of csv and feather is 15.0% of csv. In reading, parquet is 36.4% of csv and feather is 18.2% of csv. The sizes in MB are displayed above.



# Question 2
my_df.loc[my_df['US_State']=="Indiana", "Gender"].value_counts()
my_df.loc[my_df['US_State']=="Indiana", "Gender"].value_counts().plot(rot=90)
# Value_counts is applied and plot is made.



# Question 3
my_df["ConvertedCompYearly"].unique()
my_df['YearsCode']=my_df['YearsCode'].astype('str')
my_df['YearsCode']=my_df['YearsCode'].replace("[^0-9]", "", regex = True)
my_df['YearsCode']=pd.to_numeric(my_df['YearsCode'])
my_df.plot(x='YearsCode', y="ConvertedCompYearly", kind = 'scatter', logy = True)
# As the YearsCode becomes larger, the range of "ConvertedCompYearly" becomes smaller.



# Question 4
my_df["LanguageHaveWorkedWith"].unique()
my_df["LanguageHaveWorkedWith"] = my_df["LanguageHaveWorkedWith"].astype(str)
def flatten (List):
    return (item for sublist in List for item in sublist)
pd.Series(flatten(my_df["LanguageHaveWorkedWith"].str.split(";"))).value_counts()
# Times listed above. I worked with R, python, SQL, and matlab.



# Question 5
my_df.head()
my_df["SurveyEase"].unique()
my_df["SurveyEase"] = my_df["SurveyEase"].astype(str)
my_df.loc[my_df["US_State"]=="Indiana", "SurveyEase"].value_counts()
my_df.loc[my_df["US_State"]=="Indiana", "SurveyEase"].value_counts().plot(rot = 90)
# Here is how Indiana people reacted about the Survey Ease. Most people regard it as "Easy", according to the plot.


