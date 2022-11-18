# Question 1
library(data.table)
liquor <- fread("/depot/datamine/data/iowa_liquor_sales/clean_sample.csv")
dim(liquor)
liquor$Date[1] - liquor$Date[2]
liquor$date <- as.Date(liquor$Date, format="%m/%d/%Y")
class(liquor$date)
head(liquor$date)
liquor$date[1] - liquor$date[2]
# We inserted a new column that is in the "Date" class.


# Question 2
liquor$year <- format(liquor$date, "%Y")
liquor$month <- format(liquor$date, "%m")
table(liquor$month,liquor$year)
# 2012, 2013, 2014, and 2015 are covered in this dataset. All month are covered except for Dec, 2015. 


# Question 3
liquor <- fread("/depot/datamine/data/iowa_liquor_sales/clean_sample.csv")
library(lubridate)
liquor$date_b <- mdy(liquor$Date)
liquor$month_b <- month(mdy(liquor$Date))
liquor$year_b <- year(mdy(liquor$Date))
table(liquor$month_b,liquor$year_b)
head(liquor)
# I got the same result as previous questions. I prefer lubridate package because it is always good to simplify the code.


# Question 4
tapply(liquor$'Volume Sold (Gallons)', liquor$month, mean)
plot(tapply(liquor$'Volume Sold (Gallons)', liquor$month, mean), xaxt="n")
axis(side=1, at=1:12, labels=month.abb)
# As we can see, January has the lowest average sold per month. This is a little bit surprising because the temperature in Jan is extremely cold so liquor should be in great need.


# Question 5
myDF <- tapply(liquor$'Volume Sold (Gallons)', list(liquor$month, liquor$year), mean)
head(myDF)
plot(myDF[, 1], xaxt="n", col="red", type="b", xlab="Month", ylab="Sale")
axis(side=1, at=1:12, labels=month.abb)
lines(myDF[, 2], col="blue", type="b")
lines(myDF[, 3], col="green", type="b")
lines(myDF[, 4], col="black", type="b")
legend("top", legend=c("2012","2013","2014","2015"), col=c("red","blue","green","black"), lty=1 )
# As we can see, For different years, the trend of sale of liquor is different with respect to months. Especially in October, the data from 2012 and 2013 are very close, while the data from 2014 and 2015 are very close. Maybe 2014 is a turning point.


