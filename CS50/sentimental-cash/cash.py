from cs50 import get_float


def main():
    # prompt user for input
    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break
    # verify that change is 0 or not
    if change == 0:
        print(0)
    else:
        cents = round(change * 100)
        luhn(cents)
    exit(0)

# greedy function to calculate total coins


def greedy(change):
    count = [0, 0, 0, 0]
    # quarters ($0.25)
    while change >= 25:
        count[0] += 1
        change = change - 25
    # dimes ($0.10)
    while change >= 10:
        count[1] += 1
        change = change - 10
    # nickels ($0.05)
    while change >= 5:
        count[2] += 1
        change = change - 5
    # pennies ($0.01)
    while change >= 1:
        count[3] += 1
        change = change - 1
    tot = sum(count)
    print(tot)


if __name__ == "__main__":
    main()
