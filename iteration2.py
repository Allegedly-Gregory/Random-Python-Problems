


def my_loop(x):
    for y in range(0, x):
        print(y)

# my_loop(20)

def reverse_loop(num):
    reverse_list = []
    for x in range(0, num):
        reverse_list.append(x)
        rev = reverse_list[::-1]
    return rev

for x in reverse_loop(20):
    print(x)
