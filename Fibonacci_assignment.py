user_name_input = input('Input your full name: ')
print(user_name_input + ', welcome to my fibonacci')

#creatin a function for the fibonacci


def my_Fibonacci_function():
    start = int(input('Where will you like to start your Fib values from: '))
    first_value_to_be_added_to_your_input_value = 0
    no_of_el_preferred_by_user = int(input('Give the range of fibonacci you will like to print out:'))

    for i in range(no_of_el_preferred_by_user):
        the_complexity_begins = start + first_value_to_be_added_to_your_input_value
        start = first_value_to_be_added_to_your_input_value
        first_value_to_be_added_to_your_input_value = the_complexity_begins
        print(the_complexity_begins)


my_Fibonacci_function()

