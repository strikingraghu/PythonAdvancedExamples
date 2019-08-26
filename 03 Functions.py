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
