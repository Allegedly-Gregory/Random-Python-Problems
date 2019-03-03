denominations = [(100.00, 'Hundred-Dollar'), (50.00, 'Fifty-Dollar'), (10.00, 'Ten-Dollar'), (5.00, 'Five-Dollar'), (1.00, 'One-Dollar'),  (0.25, 'Quarter'), (0.10, 'Dime'), (0.05, 'Nickel'), (0.01, 'Penny')]

def show_money(num):

    output = {}
    x = float("{0:.2f}".format(num))
    print(x)
    while x > 0.001:
        for i, r in denominations:
            while x >= i:
                xyr = ''
                output[r] = output.get(r, 0) + 1
                # coutput += ","
                x -= i
                xyr += r

                # print(r, xyr.count(r))
    print(output)



show_money(12.31)
# # if output.count(r) >= 1:
            #     print(output.count("Hundreds"))
            #     print(output.count("Fifty"))
            #     print(output.count("Ten"))
            #     print(output.count("Five"))
            #     print(output.count("One"))
            #     print(output.count("Quarter"))
            #     print(output.count("Dime"))
            #     print(output.count("Nickel"))
            #     print(output.count("Penny"))
            # for name in output:
                # return name, output.count(name)
            # xyz = output
            # zarb = output.count("Hundred-Dollar"), output.count("Fifty-Dollar"), output.count("Ten-Dollar"), output.count("Five-Dollar"), output.count("One-Dollar"), output.count("Quarter"), output.count("Dime"), output.count("Nickel"), output.count("Penny")
            # if zarb >= 1:
            #     return zarb

# for x in xr:
    # print(len(x))
    # print(x[1])
