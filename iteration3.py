
# #### Challenge

# * Create a variable and assign it to the array below

# ```
# [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
# ```
# * Write a function that will take in this variable
# * It will return the median number in the array
# * It will return the average of that array
# * It will return the number that occurs most frequently in the array

# Please see the example `input` and `output` below.

# ```
# [input]
# [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

# [output]
# 9
# 14
# 8
# ```

var_1 = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]


def numbergame(lst):
    value_counts = 0
    sorted_list = sorted(lst)
    # print(sorted_list)
    len_list = len(lst)
    # print(len_list)
    index_num = (len_list - 1) // 2
    # print(index_num)
    avg = sum(lst) // len_list
    for item in lst:
        c = lst.count(item)
        if c > value_counts:
            value_counts = c
            d = item
            # last_item = value_counts[:-1]
    if len_list % 2 == 0:
        x = sorted_list[index_num]
        print(x)
        print(avg)
        print(d)
    else:
        return (sorted_list[index_num] + sorted_list[index_num + 1])/2.0




numbergame(var_1)
