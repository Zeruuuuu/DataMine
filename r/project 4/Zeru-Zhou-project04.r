# Question 1
Dataframe <- read.csv("/depot/datamine/data/olympics/athlete_events.csv")
dim(Dataframe)
table(Dataframe$Medal, useNA = "always")
prop.table(table(Dataframe$Medal, useNA = "always"))
# As the results above, there are 85.326% of athletes in olympics do not have a medal.


# Question 2
Dataframe$won_medal <- TRUE
Dataframe$won_medal[is.na(Dataframe$Medal)] <- FALSE
head(Dataframe)
# Indicator "won_medal" is added in dataframe. When no medal earned, the result is False; When medal is earned, the result is TRUE.


# Question 3
sum(is.na(Dataframe$Age))
Dataframe$age_cat <- NA
Dataframe$age_cat[Dataframe$Age < 18] <- "youth"
Dataframe$age_cat[(Dataframe$Age <= 25) & (Dataframe$Age >=18)] <- "young adult"
Dataframe$age_cat[(Dataframe$Age <= 35) & (Dataframe$Age >=26)] <- "adult"
Dataframe$age_cat[(Dataframe$Age <= 55) & (Dataframe$Age >=36)] <- "middle age adult"
Dataframe$age_cat[Dataframe$Age > 55] <- "wise adult"
head(Dataframe)
table(Dataframe$age_cat, useNA = "always")
# As Dr. Ward posted on piazza, we can use individual statement here in this question since for/if else are not good ways in R. Outputs are listed above, and there are 138333 athletes are "young adults".


# Question 4
Dataframe$age_cat_cut <- cut(Dataframe$Age, breaks = c(0,17,25,35,55,Inf), labels=c("youth","young adult","adult","middle age adult","wise adult"))
table(Dataframe$age_cat_cut, useNA = "always")
# We use cut function here to solve problem 3. The result is the same. There are 138333 athletes are "young adults".


# Question 5
prop.table(table(Dataframe$age_cat_cut[is.na(Dataframe$Medal)== FALSE]))
barplot(table(Dataframe$age_cat_cut[is.na(Dataframe$Medal)== FALSE]))
# I draw the table with proportions and barplot by breaking them into different age groups then select people who win a medal from them. As a result, I get a table of people who win a medal with different age intervals, labelled as barplot above. From barplot, there are around 20000 young adults and 15000 adults won a medal, but there are only less than 5000 medals earned by youth, middle age adult, or wise adult. As a result, young adults(18-25 years old) won most medals, wise adults(more than 55 years old) won least medals. There is association between age and winning a medal. Also, from table with proportions of those who won a medal, more than 50% of them are young adults, 40% of them are adults, and only 0.2% of them are wise adults. So there is association exists. According to the barplot and table with proportions, there is some association between age and winning a medal. Young adults(18-25 years old) won most medals, wise adults(more than 55 years old) won least medals.