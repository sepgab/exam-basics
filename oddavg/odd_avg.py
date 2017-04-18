# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(list_of_numbers):
    average_odd = 'No odd numbers in the list'
    sum_odd = 0
    counter_odd = 0
    for number in list_of_numbers:
        if number % 2 == 1:
            sum_odd += number
            counter_odd += 1
    if counter_odd > 0:
        average_odd = sum_odd / counter_odd
    return average_odd
    
