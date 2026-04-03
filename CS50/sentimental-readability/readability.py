from sys import exit


def main():
    text = input("Text: ")
    count = get_count(text)
    get_grade(count)
    exit(0)


def get_count(text):
    # count for the text
    l = s = 0
    # get number of words
    words = text.split()
    w = len(words)

    for c in text:
        # check if is alpha
        if c.isalpha():
            l += 1
        # check for end char
        if c in '.?!':
            s += 1
    # return count
    return [l, w, s]


def get_grade(result):
    L = (float(result[0]) / float(result[1])) * 100
    S = (float(result[2]) / float(result[1])) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


# call main()
if __name__ == "__main__":
    main()
