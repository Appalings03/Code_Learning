# AMEX 15         STRT 34 OR 37
# MC   16         STRT 51, 52, 53, 54, 55
# VISA 13 OR 16   STRT 4

def main():
    # prompt user for input
    while True:
        try:
            card = int(input("Card Number: "))
            if card > 0:
                break
        except ValueError:
            continue

    # convert card into str to count the length
    str_card = str(card)
    length = len(str_card)

    amex = int(str_card[:2])
    master = int(str_card[:2])
    visa = int(str_card[0])

    _sum = luhn(str_card)

    # verify that change is 0 or not
    if _sum % 10 == 0:
        # AMEX verification
        if length == 15 and amex in [34, 37]:
            print("AMEX")
        # MASTERCARD verification
        elif length == 16 and master in range(51, 56):
            print("MASTERCARD")
        # AMEX verification
        elif length in [13, 16] and visa == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
    exit(0)

# luhn function to calculate total coins


def luhn(card):
    _sum = 0
    rev_card = card[::-1]
    for i, digit_char in enumerate(rev_card):
        digit = int(digit_char)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        _sum += digit
    return _sum


if __name__ == "__main__":
    main()
