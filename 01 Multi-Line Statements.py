""" Multi-Line Statements """

# samples

a = [1, 2, 3]  # Normal way of creating a list

b = [1,
     2,
     3]  # Another way to create a list

c = [1,  # comment 1
     2,  # comment 2
     3]

d = {'key1': 1,  # comment 1
     'key2': 2  # comment 2
     }


# sample function - basics of multi-line statements


def my_func(param_a,  # comment
            param_b,  # comment
            param_c):
    print(param_a, param_b, param_c)


# few more samples
x = '''This is 'x'
defined in python code'''
print(x)

# we can simply use \ to merge both lines to one line statement
y = '''This is 'y' defined in this code to show all the variations available in python language \
to get a better sense!'''
print(y)
