def next_bigger(num: int) -> int:
    digit_of_num: list = list(str(num))
    max_num = int(''.join(map(str, sorted(digit_of_num, reverse=True))))
    min_num = int(''.join(map(str, sorted(digit_of_num))))
    my_num = num
    while my_num <= max_num:
        my_num += 1
        if int(''.join(map(str, sorted(list(str(my_num)))))) == min_num:
            return my_num
    else:
        return -1

