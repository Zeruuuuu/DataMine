# Question 1
%load_ext rpy2.ipython
%%R
my_vector <- c(1,2,3,4,5)
my_vector
my_vector = (1,2,3,4,5)
my_vector
my_tuple = (1,2,3,4,5,)
my_tuple
my_list = [1,2,3,4,5,]
my_list
import numpy as np

my_array = np.array([1,2,3,4,5])
my_array
my_tuple = (1,2,3,4,5)
my_tuple[0] = 10
my_list = [1,2,3,4,5]
my_list[0] = 10
my_list
# As we can see from the examples provided in the project, list is mutable but tuple is not. Numpy is a great package that could calculate data in dataframe form, or array.


# Question 2
my_list = [1,2,3,4,5]
my_list.append(7)
my_list.reverse()
my_list.append(6)
my_list
# As we can see, by appending 7, reversing, and then appending 6, we got the element in the list with correct order.


# Question 3
my_list[::2]
my_list[::-1]
my_list[1:4]
# As above, step 2/reverse order/got 2nd through 4th are displayed.


# Question 4
import csv
file = open('/depot/datamine/data/noaa/2020.csv')
read_file = csv.reader(file, delimiter = ',')
for row in read_file:
    print(row[3])
    break
file.close()
# The code is listed above. We got the 4th column of each row, here used break to prevent crashing.


# Question 5
import csv
with open('/depot/datamine/data/noaa/2020.csv') as my_file:
    reader = csv.reader(my_file)

    # TODO: create variable to store how many rows we've printed so far
    count = 0

    for row in reader:
        print(row)

        # TODO: increment the variable storing our count, since we've printed a row
        count += 1

        # TODO: if we've printed 10 rows, run the break statement
        if count == 10 :
            break
# As the code above, first 10 rows are printed.



