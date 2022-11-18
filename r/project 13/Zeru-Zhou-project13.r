# Question 1
library(data.table)
library(lubridate)
liquor <- fread('/depot/datamine/data/iowa_liquor_sales/clean_sample.csv')
liquor$date <- mdy(liquor$Date)
liquor$year <- year(liquor$date)
liquor$month <- month(liquor$date)
head(liquor[,c("State Bottle Cost", "State Bottle Retail")])
typeof(liquor$`State Bottle Cost`)
typeof(liquor$`State Bottle Retail`)
liquor$cost <- as.numeric(gsub('\\$', '', liquor$'State Bottle Cost'))
liquor$retail <- as.numeric(gsub('\\$', '', liquor$'State Bottle Retail'))
liquor$profit <- liquor$retail - liquor$cost
which.max(liquor$profit)
liquor$profit[1471217]
liquor[which(liquor$profit == 3000), ]
# The maximum profit is 3000 dollars.The date of these maximum profit are 10/29, 10/26, and 10/27, in 2015. The vendor names are Hy-Vee / Urbandale, Hy-Vee Food Store / Fleur / DSM, Hy-Vee Food Store #5 / Cedar Rapids, and Hy-Vee #2 / Ankeny. The number of bottle sold are 1.


# Question 2
createDashboard <- function(Number, DF) {
     myDF <- subset(DF, DF$'Vendor Number'== Number)
     barplot(tapply(myDF$profit, myDF$year, mean))  
}
createDashboard(255, liquor)
# Here above the function is created.


# Question 3
createDashboard <- function(Number, DF = liquor) {
     myDF <- subset(DF, DF$'Vendor Number'== Number) 
     par(mfrow = c(1,2))
     barplot(tapply(myDF$profit, myDF$year, mean), main= paste("Profit for Vendor", Number)) 
     barplot(tapply(myDF$'Bottle Volume (ml)', myDF$year, sum), main= paste("Bottle Volume for Vendor", Number))
}
createDashboard(255)
# Here above are the results of the modified function.


# Question 4
createDashboard <- function(Number, DF = liquor) {
     myDF <- subset(DF, DF$'Vendor Number'== Number) 
     par(mfrow = c(2,2))
     barplot(tapply(myDF$profit, myDF$year, mean), main= paste("Profit for Vendor", Number)) 
     barplot(tapply(myDF$'Bottle Volume (ml)', myDF$year, sum), main= paste("Bottle Volume for Vendor", Number))
     barplot(tapply(myDF$'Bottles Sold', myDF$month, mean), main= paste("Bottles Sold for Vendor", Number)) 
}
createDashboard(255)
# Here, the third plot is created.


# Question 5
createDashboard <- function(Number, DF = liquor) {
     myDF <- subset(DF, DF$'Vendor Number'== Number) 
     par(mfrow = c(2,2))
     barplot(tapply(myDF$profit, myDF$year, mean), main= paste("Profit for Vendor", Number)) 
     barplot(tapply(myDF$'Bottle Volume (ml)', myDF$year, sum), main= paste("Bottle Volume for Vendor", Number))
     barplot(tapply(myDF$'Bottles Sold', myDF$month, mean), main= paste("Bottles Sold for Vendor", Number)) 
     barplot(tapply(myDF$retail, myDF$month, mean), main= paste("Retail for Vendor", Number))
}
createDashboard(255)
# My plot is the average retail amount per month. From the plot we can check which months the sale condition are good and which are not.


