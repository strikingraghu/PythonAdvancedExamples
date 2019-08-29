""" Loops """


# while loop
min_length = 2
while True:
    get_name = input("Enter your name ")
    if get_name.__len__() >= 2 and get_name.isprintable() and get_name.isalpha():
        print("Hello {0}".format(get_name))
        break
    else:
        print("Provide a proper name!")


# continue loop
start_point = 0
while start_point < 10:
    start_point += 1
    if start_point % 2 == 0:
        continue
    print("Executing Continue Loop :", start_point)


# another sample
list_1 = [1, 3, 5, 7]
validate = 10
current_index = 0
while current_index < len(list_1):
    if list_1[current_index] == validate:
        break
    current_index += 1
else:
    list_1.append(validate)
print("Results :", list_1)


# another sample
var_one = 0
var_two = 2
while var_one < 4:
    var_one += 1
    var_two -= 1

    try:
        var_one / var_two
    except ZeroDivisionError:
        print("{0}, {1} - Division by 0".format(var_one, var_two))
        continue
    finally:
        print("{0}, {1} - Always executes!".format(var_one, var_two))
    print("{0}, {1} - Main loop!".format(var_one, var_two))


# another sample
list_2 = [(1, 3), (3, 5), (5, 7), (7, 9)]
for each_tuple in list_2:
    print("Each Element :", each_tuple)


# another sample
for sample1 in range(10):
    if sample1 == 7:
        break
    print("Output Sample1 :", sample1)


# another sample
for sample2 in range(10):
    if sample2 == 6:
        continue
    print("Output Sample2 :", sample2)


# another sample
for sample3 in range(1, 35):
    print("Current Value :", sample3)
    if sample3 % 7 == 0:
        print("Multiple of 7 found in this code!")
else:
    print("Multiple of 7 not found in this code!")


# another sample
string_sample = 'WOW!16CharacterZ'
loop_count = 0
for each_element in string_sample:
    print("Loop Count # =", loop_count, "|", "Value =", each_element)
    loop_count += 1


# another sample (Note Changes/Improvisation)
sample4 = "WOW!16CharacterZ"
for curr_index, curr_index_val in enumerate(sample4):
    print("Index =", curr_index, "|", "Value =", curr_index_val)
