try:
    pounds = float(input("Weight in pounds: "))
except ValueError:
    print("Not a number")
else:
    kilograms = pounds * 0.454
    print("%s pounds is %s kilograms" % (pounds, kilograms))