season1 = 10 * (45 * 60 + 35)          # 10 episodes at 45m 35s
other_seasons = 4 * 10 * (35 * 60 + 15)  # 4 seasons, 10 episodes at 35m 15s
total = season1 + other_seasons

hours = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60

print("Total time: %dh %dm %ds" % (hours, minutes, seconds))