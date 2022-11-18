# Question 1
library(data.table)
books <- fread("/depot/datamine/data/goodreads/csv/goodreads_books.csv")
head(books)
sort(tapply(books$average_rating, books$publication_month, mean, na.rm=T), decreasing=T)
# As a result, average rating is highest in November and lowest in January, according the table listed above. I suggest Dr. Ward publish his work in November because the rating (3.896) is relative higher than the other months across the whole year.


# Question 2
summary(books$num_pages)
books$book_size_cat <- cut(books$num_pages, breaks= c(0, 100, 400, Inf), include.lowest=T, useNA="always", labels= c("small","medium","large"))
table(books$book_size_cat, useNA= "always")
# In above, I use Dr.Ward's break period to justify my method is correct. Then I'm gonna use my break period.
books$book_size_cat <- cut(books$num_pages, breaks= c(0, 145, 345, Inf), include.lowest=T, useNA="always", labels= c("small","medium","large"))
table(books$book_size_cat,useNA="always")
summary(books$num_pages)
hist(books$num_pages)
hist(books$num_pages[books$num_pages <= 1000])
boxplot(books$num_pages[books$num_pages < 4000])
# I pick [0,145] as small since the first quarter is 147, so I just find a number 145 near it to define as "small". Then, I pick [145,345] as medium since the third quarter is 344, I find a number 345 near it to divide the boundry between medium and large. Then, if the number id greater than 345, it is defined as large because it is larger than 3/4 of the data. The result of running "table(books$book_size_cat)" is listed above.



# Question 3
tapply(books$text_reviews_count, books$book_size_cat, mean)
# As the table above, we see that text reviews are far more in category "large" than in "medium" or "small". Therefore, as a firm believer in feedback, Dr. Ward should consider about large size as book size, which is more than 345 pages in my division in last problem.



# Question 4
boxplot(text_reviews_count~book_size_cat, data= books)
# My answer won't change based on the boxplot because "large" is still category that owns more reviews, and "small" has obviously less reviews than the other categorys. So, I would still recommand "large" book size. To be honest, the box is hard to read because the value beyond the box is so large that I can hardly see the box.



# Question 5
boxplot(text_reviews_count~book_size_cat, data= subset(books, text_reviews_count<200))
# The box is shown up since we use a smaller data set to concentrate on smaller values. It is easier to read than before, and from the plot, we can see that large box has obviously larger number of reviews than medium and small.


# Question 6
authors <- fread("/depot/datamine/data/goodreads/csv/goodreads_book_authors.csv")
dim(authors)
names(authors)
names(authors) %in% names(books)
books_authors <- merge(books,authors, by.x="author_id", by.y="author_id")
dim(books_authors)
Sub <- subset(books_authors, name %in% c("Douglas Adams","Lloyd Alexander","William Shakespeare","John Donne","John Keats"))
dim(Sub)
names(Sub)
boxplot(text_reviews_count.x ~ book_size_cat, data= Sub)
boxplot(text_reviews_count.x ~ book_size_cat, data= subset(Sub, text_reviews_count.x <200 ))
# As we can see, recommandation should change to "medium" book size when we concentrate on these 5 authors: Douglas Adams, Lloyd Alexander, William Shakespeare, John Donne, and John Keats. In both original and restricted boxplot, "medium" book size seems to have greater number of reviews than "large" and "small". Thus, I would rather recommand "medium" book size here.



