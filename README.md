# Three variables are created (avg, total, top), each variable containing a lambda expression which calculates either average, total or top of the grades.
# The three variables which contain the functionalities are then stored in a dictionary, which will then be checked and applied, once the user provided the input.
# The "students" list contains 4 dictionaries, which are then organised in two sets of key-value pairs.
# The "grades" are stored as tuple, because they will no longer change (the reason I have not chosen sets, is because sets house only unique data structures, therefore, if the student(s) would receive a second similar grade, the value will be ignored)
# The for loop goes over the students list of dictionaries, and two variables have been created, which will contain the name and the grades of each student.
# The variable "operation" will store the input of the user/student.
# The condition will then check if the input provided by the user is contained in the operations dictionary created beforehand, and if it is included, then it will calculate either the average, total or top, depending on the user's choice, but if the input was not found, the it will print out "Does not exist."
