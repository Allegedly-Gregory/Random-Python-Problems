

def fizzbuzz(int):
    for x in range(0, int+1):
        if x % 3 == 0 and int % 5 == 0:
            print("FizzBuzz")
        else:
            if x % 3 == 0:
                print("Fizz")
            else:
                if x % 5 == 0:
                    print("Buzz")
                else:
                    print(x)


fizzbuzz(20)















