"""
Alphabet Soup:
    function takes str as rguments and arrange the letters in
    alphebetical(ascending) order
"""


# Naive Solution - 1 (using sorted - builtin method)
def alphabet_soup_with_sorted(strValue):
    if len(strValue) <= 1:
        return strValue
    return "".join(sorted(strValue))


def quick_sort(strValue):

    length = len(strValue)
    if length < 1:
        return strValue
    pivot = strValue[(length // 2)]
    left = [i for i in strValue if pivot > i]
    right = [i for i in strValue if pivot < i]
    middle = [i for i in strValue if pivot == i]

    return quick_sort(left) + middle + quick_sort(right)


def alphabet_soup_with_quicksort(strValue):

    if len(strValue) <= 1:
        return strValue
    return "".join(quick_sort(strValue))  # call the quick sort function here


# Test the function
print(alphabet_soup_with_sorted("dcba"))
print(alphabet_soup_with_sorted("hello"))
print(alphabet_soup_with_sorted("python"))


print(alphabet_soup_with_quicksort("hello"))
