# Question 2
system("hostname", intern = TRUE )
# I'm running on the node brown-a008.rcac.purdue.edu

# Question 5
550*24
550*96

# Question 6
dat <- read.csv("/depot/datamine/data/disney/splash_mountain.csv")
head(dat)
splash_mountain <- dat
rm(dat)
# I run the given code and read the dataset. The output includes date, datetime, SACTMIN, and SPOSTMIN 4 columns as total. After renaming, the dataset "dat" has its new name as "splash_mountain".
