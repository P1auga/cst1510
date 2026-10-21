name = input("Employee name: ")

try:
    hours = float(input("Hours worked: "))
    rate = float(input("Hourly rate: "))
    federal = float(input("Federal tax rate (%): "))
    state = float(input("State tax rate (%): "))
except ValueError:
    print("Numeric values required")
else:
    gross = hours * rate
    federal_withholding = round(gross * federal / 100, 2)
    state_withholding = round(gross * state / 100, 2)
    net = round(gross - federal_withholding - state_withholding, 2)

    print("Employee:", name)
    print("Gross pay: £%.2f" % gross)
    print("Federal withholding: £%.2f" % federal_withholding)
    print("State withholding: £%.2f" % state_withholding)
    print("Net pay: £%.2f" % net)