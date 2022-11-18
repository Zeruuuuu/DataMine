# Question 1
us_youtube <- read.csv("/depot/datamine/data/youtube/USvideos.csv")
dim(us_youtube)
head(us_youtube$trending_date)
library(lubridate)
# First, change the format of those columns to date.
us_youtube$trending_date <- ydm(us_youtube$trending_date)
us_youtube$publish_time <- ymd_hms(us_youtube$publish_time)
# Second, extract the year from the columns.
us_youtube$trending_year <- year(us_youtube$trending_date)
us_youtube$publish_year <- year(us_youtube$publish_time)
unique(us_youtube$trending_year)
unique(us_youtube$publish_year)
table(us_youtube$trending_year)
table(us_youtube$publish_year)
class(us_youtube$trending_year)
typeof(us_youtube$trending_year)
class(us_youtube$publish_year)
typeof(us_youtube$publish_year)
# Test vectorized (They are all vectorized since they are all run on full vector of data.) 
head(us_youtube$trending_date)
head(year(us_youtube$trending_date))
# Without using functions above
us_youtube <- read.csv("/depot/datamine/data/youtube/USvideos.csv")
us_youtube$trending_year <- as.numeric(paste0("20", substr(us_youtube$trending_date, 1, 2)))
table(us_youtube$trending_year)
head(us_youtube$trending_year)
us_youtube$publish_year <- as.numeric(substr(us_youtube$publish_time, 1, 4))
table(us_youtube$publish_year)
head(us_youtube$publish_year)
# All the results are expanded above. The new columns are double type and numeric class. In the provided code, all the functions are vectorized since they all run on full vector data. I got exactly the same results without using functions like "ydm", "year", "ymd_hms", and "unique", and I found that those functions such as "ydm" and "year" builds a much easier way.


# Question 2
dataframe <- function(mycountry) {
    DF <- read.csv(paste0("/depot/datamine/data/youtube/", mycountry, "videos.csv"))
    DF$country_code <- mycountry
    return(DF)
    }
Countries <- c('CA', 'DE', 'FR', 'GB', 'IN', 'JP', 'KR', 'MX', 'RU', 'US')
Applied_results <- lapply(Countries, dataframe)
yt <- do.call(rbind, Applied_results)
dim(yt)
colnames(yt)
library(lubridate)
yt$trending_year <- year(ydm(yt$trending_date))
yt$publish_year <- year(ymd_hms(yt$publish_time))
# Column "country code" is added. Columns of yt is printed, and yt has 375942 rows and 17 columns. Columns trending_year and publish_year is created.


# Question 3
table(yt$publish_year)
yt$trending_date <- ydm(yt$trending_date)
yt$publish_time <- ymd_hms(yt$publish_time)
table(yt$trending_year)
yt[yt$publish_year == 2006, ]
# The name (title) of the video is "Budweiser - Original Whazzup? ad", and it took 2018-2006=12 years to trend.


# Question 4
table(yt$ratings_disabled)
yt$ratings_disabled_combined <- NA
yt$ratings_disabled_combined[yt$ratings_disabled == "FALSE"] <- FALSE
yt$ratings_disabled_combined[yt$ratings_disabled == "False"] <- FALSE
yt$ratings_disabled_combined[yt$ratings_disabled == "TRUE"] <- TRUE
yt$ratings_disabled_combined[yt$ratings_disabled == "True"] <- TRUE
table(yt$ratings_disabled_combined, useNA="always")
class(yt$views)
tapply(yt$views, yt$ratings_disabled_combined, mean)
# The average number of views for videos with ratings enabled and those with ratings disabled are 1338148 and 742479, respectively. As a result, it looks like disabling the rating hurts the views.


# Question 5
yt$balance <- (yt$likes) - (yt$dislikes)
yt$positive_balance <- NA
yt$positive_balance[yt$balance > 0] <- TRUE
yt$positive_balance[yt$balance <= 0] <- FALSE
table(yt$positive_balance, useNA="always")
# There are 361583 videos that have a positive balance.# 


# Question 6
tapply(yt$comment_count, yt$positive_balance, mean )
tapply(yt$views, yt$positive_balance, mean)
# I choose mean as the statistic for both comment_count and views. This is because the mean shows the average level of the number of views/comments that could be compared between different groups of data (In this case, there are 2 groups: with and without positive balance). The videos with positive balance tends to have much more views and slightly more comments than videos without positive balance.







