# # Don't Hesitate, Iterate... part 2!

# #### Description

# Practice makes perfect. Here's some practice with iteration and lists.

# ---

# #### Challenge

# * Create a variable and assign it to a list of various data types.
# * Write a function that will take in this variable.
# * The function will loop through the list and print all the values to the terminal individually.

# We're not giving you any starter code this time. Sorry! Checkout the starter code in `iteration with lists` for some example starter code that will help you setup this challenge.

# Here's some example `input` and `output`:

# [output]
# 1
# 2
# jeff
# tom
# 42
# billy
# jason
# ```
# ```
var_list = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]


def lister(lst):
    new_lst = []
    for x in lst:
        new_lst.append(x)
        # for i in str(x):
        #     new_lst.append(i)
        # # new_lst.append(x)
    x = new_lst[0]
    y = new_lst[1]
    jeff = new_lst[2][0]
    tom = new_lst[2][1]
    z = new_lst[3][0]
    billy = new_lst[3][1][0]
    jason = new_lst[3][1][1]
    print(x)
    print(y)
    print(jeff)
    print(tom)
    print(z)
    print(billy)
    print(jason)

lister(var_list)




