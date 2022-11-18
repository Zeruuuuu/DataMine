# Question 1
list.files("/depot/datamine/data/olympics")
dim(read.csv("/depot/datamine/data/olympics/athlete_events.csv"))
dim(read.csv("/depot/datamine/data/olympics/regions.csv"))
olympics <- read.csv("/depot/datamine/data/olympics/athlete_events.csv")
dim(olympics)
head(olympics)
str(olympics)

# Olympics has 271116 rows and 15 columns, and there are 3 types of data: integer, numeric and character. Each row contains basic information about a specific athlete.


# Question 2
length(unique(olympics$Sport))
unique(olympics$Sport)
# There are 66 unique sports in the dataset olympics. I use 'unique' function to show unique individual sports included in the dataset. There are some sports I never expected like 'Motorboating' since I thought it is more like a hobby and just for fun. Never expected it is on olympics.


# Question 3
us_athletes <- subset(olympics, NOC=='USA')
dim(us_athletes)
china_athletes <- subset(olympics, NOC=='CHN')
dim(china_athletes)
both <- subset(olympics, NOC=='USA'| NOC=='CHN')
dim(both)
# There are 18853 rows in 'us_athletes' dataset; There are 5154 rows in dataset contains athletes from China named 'china_athletes'; There are 23994 rows in 'both' dataset.


# Question 4
prop.table(table(olympics$Sex[olympics$NOC=='USA']))
prop.table(table(olympics$Sex[(olympics$NOC=='USA') & (olympics$Medal=='Gold')]))
prop.table(table(olympics$Sex[olympics$NOC=='CHN']))
prop.table(table(olympics$Sex[(olympics$NOC=='CHN') & (olympics$Medal=='Gold')]))
# 29.35% athletes in the US are women; 32.30% athletes in the US with gold medals are women. 53.88% athletes in China are women; 60% athletes in China with gold medals are women.


# Question 5
us_athletes <- subset(olympics, NOC=='USA')
us_age <- us_athletes$Age
which.max(us_age)
us_athletes[which.max(us_age), c('Age', 'Sport', 'Year')]
china_athletes <- subset(olympics, NOC=='CHN')
ch_age <- china_athletes$Age
which.max(ch_age)
china_athletes[which.max(ch_age), c('Age', 'Sport', 'Year')]
# For the US, the oldest athlete is 97 years old, the sport is 'Art Competitions', and the olympics year is 1928. For China, the oldest athlete is 45 years old, the sport is 'Equestrianism', and the olympics year is 2008.