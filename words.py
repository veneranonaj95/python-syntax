def print_upper_words1(words):
    """Print words uppercased, on sepparate lines.

        >>>print_upper_words(["bastille", "movies", "popcorn", "hero"])
    """
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print words uppercased, on sepparate lines, only if they start with "e"

        >>>print_upper_words(["errosion", "earl", "Cucumber", "Snickers"])
    """
    for word in words:
        if word.startswith("e"):
            print(word.upper())


def print_upper_words3(words):
    """Print each word that starts with T or c, as uppercased, on a sepparate line.

        >>>print_upper_words2(["Throne", "Thomas", "candle", "Candies", "october"])
    """
    for word in words:
        if word.startswith("T") or word.startswith("c"):
            print(word.upper())

