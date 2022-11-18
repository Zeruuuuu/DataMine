# Question 1
library(data.table)
elections <- fread("/depot/datamine/data/election/itcont2014.txt", sep="|")
benfords_law_old <- function(digit) {
    if ((digit < 1) | (digit > 9)) {stop("digit is out of range")}
    log((digit+1)/digit)/log(10)

}
benfords_law <- function(v) {
    sapply(v, benfords_law_old)
}
get_starting_digit <- function(transaction_vector) {
    as.numeric(substr(transaction_vector,1,1))
}
T <- table(get_starting_digit(elections$TRANSACTION_AMT)[elections$TRANSACTION_AMT != 0])
plot(T/sum(T))
lines(benfords_law(1:9))
# There are modifications needed because 0 is included in our dataset but benfords law only accept 1 to 9. We need to remove 0 when analyzing.


# Question 2
T <- table(get_starting_digit(elections$TRANSACTION_AMT)[elections$TRANSACTION_AMT != 0])
plot(T/sum(T),main="Comparison under Benfords law")
lines(benfords_law(1:9))
# This should not be considered as anomalous because except for starting value 2 and 5, the rest of digits are following benfords law. This is because maybe many transactions are like $500, or $2000. Benfords law aimed to analyze real world data and this should be normal case.



# Question 3
compare_to_benfords <- function(values,title="Comparison under Benfords law") {
        T <- table(get_starting_digit(values)[values != 0])
        plot(T/sum(T), main=title)
        lines(benfords_law(1:9))
}
compare_to_benfords(elections$TRANSACTION_AMT)
# Here I combined the process together and created function "compare_to_benfords". The result is exactly the same as in question 2.


# Question 4
par(mfrow=c(1,3))
compare_to_benfords(elections$TRANSACTION_AMT[elections$ENTITY_TP=="CAN"],"Benford for CAN")
compare_to_benfords(elections$TRANSACTION_AMT[elections$ENTITY_TP=="IND"],"Benford for IND")
compare_to_benfords(elections$TRANSACTION_AMT[elections$ENTITY_TP=="ORG"],"Benford for ORG")
# The transaction amount in each entity are combined into one graph, as shown above.


# Question 5
names(elections)
head(elections)
par(mfrow=c(2,2))
compare_to_benfords(elections$TRANSACTION_AMT[elections$STATE=='VA'],"Benford for Virginia")
compare_to_benfords(elections$TRANSACTION_AMT[elections$STATE=='PA'],"Benford for Pennsylvania")
compare_to_benfords(elections$TRANSACTION_AMT[elections$STATE=='IL'],"Benford for Illinois")
compare_to_benfords(elections$TRANSACTION_AMT[elections$STATE=='IN'],"Benford for Indiana")
# I compared transaction amount in four states: VA, PA, IL, and IN, with benfords law appears to check anormality. I find that these four states has extremely similiar pattern in the percentage pattern of transaction amount when checking the first digit. Transactions with starting digits 2 and 5 are extremely common in all of the four states. Also, except for these two digits, the others follows the benfords law tightly.



