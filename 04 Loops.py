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
