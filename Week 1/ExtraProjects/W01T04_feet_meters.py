try:
    feet = float(input("Length in feet: "))
except ValueError:
    print("Not a number")
else:
    meters = feet * 0.305
    print("%s feet is %s meters" % (feet, meters))