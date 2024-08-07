"""
Alphabet Soup:
    function takes str as rguments and arrange the letters in
    alphebetical(ascending) order
"""


# Naive Solution - 1 (using sorted - builtin method)
def alphabet_soup_with_sorted(strValue):
    return "".join(sorted(strValue))


print(alphabet_soup_with_sorted("hello"))
