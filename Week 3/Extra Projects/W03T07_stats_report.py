import statistics as stats


def get_mean(values):
    return stats.mean(values)


def get_median(values):
    return stats.median(values)


def get_std_dev(values):
    return stats.stdev(values)


def main():
    raw = input("Enter five numbers separated by spaces: ")
    values = [float(x) for x in raw.split()]
    if len(values) != 5:
        print("Please enter exactly five numbers.")
        return

    print("Values: " + ", ".join(f"{v:g}" for v in values))
    print(f"Total = {sum(values):.2f}")
    print(f"Mean = {get_mean(values):.2f}")
    print(f"Median = {get_median(values):.2f}")
    print(f"Std Dev = {get_std_dev(values):.2f}")


if __name__ == "__main__":
    main()
