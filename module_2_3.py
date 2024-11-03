my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
first_value = 0
while first_value <= len(my_list):
    if my_list[first_value] > 0:
        print(my_list[first_value])
        first_value += 1
        if my_list[first_value] == 0:
            first_value += 1
        continue
    break