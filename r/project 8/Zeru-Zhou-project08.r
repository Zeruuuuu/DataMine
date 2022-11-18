# Question 1
library(data.table)
interactions <- fread("/depot/datamine/data/goodreads/csv/interactions_subset.csv")
# A function that, given a string (userID) and a value (min_rating) returns a value (probability_of_reviewing).
get_probability_of_review <- function(interactions_dataset, userID, min_rating) {
        # Filtering the dataset and keep data that has user_id equals to the given userID. Name the filtered dataset user_data.
        user_data <- subset(interactions_dataset, user_id == userID)

        # Filtering the dataset once more to keep data that has is_read column equals to 1. Name the filtered dataset read_user_data.
        read_user_data <- subset(user_data, is_read == 1)

        # Filtering the dataset once more to keep data that has rating column more than the given min_rating. Name the filtered dataset read_user_min_rating_data.
        read_user_min_rating_data <- subset(read_user_data, rating >= min_rating)

        # Define probability_of_reviewing as the mean of the is_reviewed column in dataset read_user_min_rating_data.
        probability_of_reviewing <- mean(read_user_min_rating_data$is_reviewed)

        # Return the result
        return(probability_of_reviewing)
}

get_probability_of_review(interactions_dataset = interactions, userID = 5000, min_rating = 3)
# This function takes interactions_dataset, userID, and min_rating as inputs, and probability of reviewing as output. It uses userID, and min_rating to filter the dataset, then calculating the mean of is_reviewed column of the filtered dataset. It has 3 arguments: interactions_dataset, userID, and min_rating.



# Question 2
get_probability_of_review <- function(interactions_dataset, userID, min_rating=0) {
        # Filtering the dataset and keep data that has user_id equals to the given userID. Name the filtered dataset user_data.
        user_data <- subset(interactions_dataset, user_id == userID)

        # Filtering the dataset once more to keep data that has is_read column equals to 1. Name the filtered dataset read_user_data.
        read_user_data <- subset(user_data, is_read == 1)

        # Filtering the dataset once more to keep data that has rating column more than the given min_rating. Name the filtered dataset read_user_min_rating_data.
        read_user_min_rating_data <- subset(read_user_data, rating >= min_rating)

        # Define probability_of_reviewing as the mean of the is_reviewed column in dataset read_user_min_rating_data.
        probability_of_reviewing <- mean(read_user_min_rating_data$is_reviewed)

        # Return the result
        return(probability_of_reviewing)
}
get_probability_of_review(interactions_dataset = interactions, userID = 5000)
get_probability_of_review(userID = 5000,interactions_dataset = interactions)
get_probability_of_review(interactions, 5000)
# Here is modified: min_rating=0 at the start of the function. 


# Question 3
get_probability_of_review <- function(interactions_dataset, userID, min_rating=0) {
        # Filtering the dataset 
        read_user_min_rating_data <- subset(interactions_dataset, (user_id == userID) & (is_read == 1) & (rating >= min_rating))

        # Define probability_of_reviewing as the mean of the is_reviewed column in dataset read_user_min_rating_data.
        probability_of_reviewing <- mean(read_user_min_rating_data$is_reviewed)

        # Return the result
        return(probability_of_reviewing)
}
get_probability_of_review(interactions, 5000)
# Code is reduced above. Now we only use 1 subset.



# Question 4
head(read_user_min_rating_data)
# There is an error that there do not exist something called "read_user_min_rating_data", so there comes an error when running head function on it. This is because "read_user_min_rating_data" is an dataset we defined that only make sense inside our "get_probability_of_review" function. That is, it could not be used or detected outside "get_probability_of_review" function, so there is an error when directly use it outside the function "get_probability_of_review".




# Question 5
boxplot(interactions$rating)
users <- sample(interactions$user_id, 10)
users
prob_review <- sapply(users, function(m) get_probability_of_review(interactions_dataset=interactions, userID=m, min_rating=0))
prob_review
# The results are listed above. I pick 0 as the specific minimum rating value because according to boxplot I drew, there are many data that has rating value of 0. If we choose another number greater than 0 then it should not be called "minimum" rating value.                
                      
                      
# Question 6
prob_review1 <- sapply(users, function(m) get_probability_of_review(interactions_dataset=interactions, userID=m, min_rating=1))
prob_review1
plot(prob_review, prob_review1)
# For each of the 10 users, the horizontal axis represents probability when min_rating is 0. The vertical axis represents the probability when min_rating is 1. As we can see, the value of probability is almost the same except for a couple of users with probability between 0.3 and 0.5. Hence, changing the value of min_rating affects the outcome of probability, but maybe slightly as my result above.
                       
                       
                       
                       