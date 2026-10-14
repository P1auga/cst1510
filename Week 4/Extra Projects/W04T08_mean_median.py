def get_mean(data):
    return sum(data) / len(data)

def get_median(data):
    ordered = sorted(data)
    return ordered[len(ordered) // 2]

regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]

for data in (regular_data, outlier_data):
    print(data, "mean:", get_mean(data), "median:", get_median(data))
