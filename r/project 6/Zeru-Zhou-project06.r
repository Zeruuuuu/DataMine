# Question 1
tracks <- read.csv("/depot/datamine/data/amazon/tracks.csv")
dim(tracks)
str(tracks)
tracks <- read.csv("/depot/datamine/data/amazon/tracks.csv",sep="|")
dim(tracks)
str(tracks)
head(tracks)
# We can see that originally it has only 1 column, and there are many "|" in that column; After using "sep" when reading the data, there are 14 columns now being seperated by "|", and "str" command gives us information about each column.


# Question 2
library(RSQLite)

con <- dbConnect(SQLite(), dbname = "/depot/datamine/data/amazon/tracks.db")
myDF <- dbGetQuery(con, "SELECT year, AVG(duration) AS average_duration FROM songs GROUP BY year;")
head(myDF)
head(tapply(tracks$duration, tracks$year, mean))
# As we can see, the results of the given code is exactly the same as the result if we use tapply function.


# Question 3
G <- tapply(tracks$duration, tracks$year, mean)
length(G)
plot(as.numeric(names(G))[2:90], G[2:90])
# Except for several outliers, as the time goes by, the duration of musics is became longer and longer. (As the year increases, duration increases, in the general trend).


# Question 4
head(tapply(tracks$duration, tracks$artist_name, median))
head(sort(tapply(tracks$duration, tracks$artist_name, median), decreasing=T))
# The artist_name with the highest median duration is "Ustad Rashid Khan". The 5 results sorted in decreasing order is listed above.


# Question 5
# Question: Plot the average duration with respect to artist_hotttnesss. Are there any patterns? What is the artist_hotttnesss of the lowest average duration?
H <- tapply(tracks$duration, tracks$artist_hotttnesss, mean)
length(H)
plot(as.numeric(names(H)[2:43476]),H[2:43476])
head(sort(H))
# As the result, the plot shows no obvious pattern but extremely high durations have artist_hotttnesss in range between 0.2 and 0.5. The artist_hotttnesss of the lowest average duration is around 0.3465, as calculated above.


# Question 6
# Average duration with respect to different artist_familiarity
library(RSQLite)

con <- dbConnect(SQLite(), dbname = "/depot/datamine/data/amazon/tracks.db")
myDF <- dbGetQuery(con, "SELECT artist_hotttnesss, AVG(duration) AS average_duration FROM songs GROUP BY artist_hotttnesss;")
head(myDF)
length(myDF$artist_hotttnesss)
plot(myDF$artist_hotttnesss[2:43476], myDF$average_duration[2:43476])
# I got the same result as in question# 5, using the SQL code provided.


