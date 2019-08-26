""" Functions """


def func_1(a, b):
    print(a, b)


func_1(5, 10)


def func_2():
    return func_3()


def func_3():
    print('running func_3')


# difference in output should be noticed
func_2()
print(func_2)

# lambda
func1 = lambda x: x ** 5
print(func1(2))

# few more examples


def calculate_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calculate_factorial(x-1)


sample_value = 8  # Testing function!
print("Processed Factorial Function =", calculate_factorial(sample_value))  # 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1

