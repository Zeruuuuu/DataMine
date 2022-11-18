# Question 1
stations <- read.csv("/depot/datamine/data/whin/stations.csv")
weather <- read.csv("/depot/datamine/data/whin/weather.csv")
head(stations)
head(weather)
tail(stations)
tail(weather)
str(stations)
str(weather)
names(stations)
names(weather)
dim(stations)
dim(weather)
summary(stations$id)
summary(weather$rain)
# Code and outputs are listed above, including read.csv function and some functions like head(), tail(), dim(), summary(), str(), and names(). Answering questions: The dimension of dataset "stations" is 178 rows and 4 columns. The dimension of dataset "weather" is 1000000 rows and 26 columns. The first 5 rows are listed above in the code: head(stations) and head(weather). The column names are displayed above in the code: names(stations) and names(weather).


# Question 2
temp <- weather$temperature
head(temp)
temp[100]
tail(temp)
typeof(temp)
class(temp)
# Code and output are displayed above. The first value in the vector temp is 70; the 100th value is 63; the last value is 64. The type of data in the vector is Double data type. The class of data is numeric.


# Question 3
temp100 <- head(weather$rain_inches_last_hour,n=100)+tail(weather$rain_inches_last_hour,n=100)
# One line code is above code, since I see we do not need to print temp100 on piazza, we do not have output through this one line code. It only add them together and form a new vector.


# Question 4
Sub <- subset(weather, station_id == 20)
hot_temps <- Sub$temperature[Sub$temperature >= 85]
length(hot_temps)
head(hot_temps)
cold_temps <- Sub$temperature[Sub$temperature <= 40]
length(cold_temps)
head(cold_temps)
head(hot_temps+cold_temps)
# Hot_temps and cold_temps are created above. There are 909 elements in hot_temps and 20627 elements in cold_temps. If I add them together, an error occurs : “longer object length is not a multiple of shorter object length”. This is because when two vector are added, the shorter one would be recycled until it matches to the length of the longer vector.


# Question 5
myRain <- weather$rain[weather$station_id == 20]
plot(head(myRain,300))
mySolar <- weather$solar_radiation[weather$station_id == 20]
plot(head(mySolar,300))
# I tried to plot on station_id=20 and column rain and solar_radiation seperately. For plot for column rain, the pattern is that rain does not deviate from 0 with the change in index. There are only few cases that rain is not 0, and I think they could be outliers. For plot for column solar_radiation, the pattern is fluctuating with index. Going down first, and remain at solar_radiation=0 for around 50 indexs, then going up and repeat this procedure for many times as index move forward.