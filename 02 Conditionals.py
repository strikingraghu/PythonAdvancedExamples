""" Conditionals """


# samples
a = 6
if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')


# ternary operator
a, b = 10, 20
get_output = a if a < b else b
print("Ternary Output :", get_output)

age = 12
results = "Minor" if age < 21 else "Adult"
print("Ternary Output :", results)

another_output = ({True: a, False: b}[a < b])
print("Ternary Output :", another_output)
