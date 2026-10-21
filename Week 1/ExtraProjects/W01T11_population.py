population = 312032486
seconds_per_year = 365 * 24 * 60 * 60

births = seconds_per_year // 7
deaths = seconds_per_year // 13
immigrants = seconds_per_year // 45
change = births - deaths + immigrants

for year in range(1, 6):
    print("Year %d: %s" % (year, format(population + change * year, ",")))