# Question 11
library(lubridate)

countries <- c('US', 'DE', 'CA', 'FR')

# Choose either the for loop or the sapply function for creating `yt`

# EITHER use a for loop to create the data frame `yt`
yt <- data.frame()
for (c in countries) {
    filename <- paste0("/depot/datamine/data/youtube/", c, "videos.csv")
    dat <- read.csv(filename)
    dat$country_code <- c
    yt <- rbind(yt, dat)
}
dim(yt)
# OR use an sapply function to create the data frame `yt`
myDFlist <- lapply( countries, function(c) {
                    dat <- read.csv(paste0("/depot/datamine/data/youtube/", c, "videos.csv"))
                    dat$country_code <- c
                    return(dat)} )
yt <- do.call(rbind, myDFlist)
dim(yt)
# convert columns to date formats
yt$trending_date <- ydm(yt$trending_date)
yt$publish_time <- ymd_hms(yt$publish_time)

# extract the trending_year and publish_year
yt$trending_year <- year(yt$trending_date)
yt$publish_year <- year(yt$publish_time)

count_tags <- function(tag_vector){
    length(strsplit(tag_vector, "|", fixed=TRUE)[[1]]) 
    }
tag_test <- yt$tags[2]
tag_test
count_tags(tag_test)
# The function count_tags is created and the example has 4 unique tags.

# Question 12
yt$n_tags <- sapply(yt$tags, count_tags)
head(yt)
US_DE <- subset(yt, (country_code=='US')|(country_code=='DE'))
dim(US_DE)
US_DE$video_id[which.max(US_DE$n_tags)]
US_DE$title[which.max(US_DE$n_tags)]
US_DE$n_tags[which.max(US_DE$n_tags)]
# The title is 'TOP 20 SINGLE CHARTS ►27. Dezember 2017 [FullHD]', and the number of tags it contains is 97.

# Question 3
plot(US_DE$views, US_DE$n_tags)
plot(tapply(US_DE$views, US_DE$n_tags, median))
# Scatter plot is a little bit messed up. I can only know that it is not a fully positive correlation. By using tapply function and use the median to evaluate the number of views under different number of tags, we can clearly see that when the number of tags is around 40, the median of the number of views is the highest.

# Question 4
plot(tapply(yt$views, yt$country, mean), tapply(yt$comment_count, yt$country, mean))
tapply(yt$views, yt$country, mean)
tapply(yt$comment_count, yt$country, mean)
table(yt$country)
# Here we compared the mean value of the views and number of comment with respect to different countries. We can see that the more the average views, the more the average number of comments. It is fair because we are comparing the mean value, and also the samples we collect for each country are approximately the same (almost 40900). 

# Question 5
tapply(yt$n_tags, yt$country, mean)
tapply(yt$likes, yt$country, mean)
plot(tapply(yt$n_tags, yt$country, mean), tapply(yt$likes, yt$country, mean))
# My logic is that the more number of tags, there should be more "likes" because it is more conclusive with many tags. Let's compare those four countries: as we can see, this trend is perfectly applied on this dataset. The country with more average number of tags has more average number of likes. Also, to compare these four countries horizontally, the US has the largest average number of tags and likes, and France has the least average number of tags and likes.

