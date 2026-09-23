weeks = 3 * 52

savings = 0.0
savings += weeks * 10        # weekly deposits
savings += 52 * 20           # year 1 bonus
savings -= (weeks / 2) * 0.50  # sister, every 2 weeks

print("Final savings after 3 years: £%.2f" % savings)