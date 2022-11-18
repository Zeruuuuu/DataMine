# Question 1
benfords_law <- function(digit) {log((digit+1)/digit)/log(10)}
sapply(1:9, benfords_law)
benfords_law(7)
# Benfords_law is created as a function. When digit is 7, the value returned is 0.05799.


# Question 2
benfords_law <- function(digit) {
    if ((digit < 1) | (digit > 9)) {stop("digit is out of range")}
    log((digit+1)/digit)/log(10)

}
benfords_law(0)
# Error catching statement is added. When running benfords_law(0), the error message shows up.


# Question 3
benfords_law_old <- function(digit) {
    if ((digit < 1) | (digit > 9)) {stop("digit is out of range")}
    log((digit+1)/digit)/log(10)

}
benfords_law <- function(v) {
    sapply(v, benfords_law_old)
}
benfords_law(0:5)
benfords_law(1:6)
# Here we see we vectorized the function by sapply function. Results are listed above.


# Question 4
benfords_law(1:9)
plot(benfords_law(1:9), xlab="digits", main="Benford’s law in lineplot", type="b")
barplot(benfords_law(1:9), main="Benford’s law in Barplot", xlab="digits", names.arg=c("1","2","3","4","5","6","7","8","9"))
# Here are the lineplot and barplot of the benford's law of all digits.


# Question 5
get_starting_digit <- function(transaction_vector) {
    as.numeric(substr(transaction_vector,1,1))
}
get_starting_digit(c(10,400,535))
str(get_starting_digit(c(100,2,50,689,1)))
# Here I use substr function to get the first digit and as.numeric function to convert it as numeric value. 


