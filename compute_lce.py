import compare_complimentary


# returns the length of the longest common extension starting at string[n1] and reverse string[n2]
def lce_query(length, string, str_reverse, n1, n2):
    count = 0
    while (n1 + count < length and n2 + count < length
           and string[n1 + count] == str_reverse[n2 + count]):
        count += 1
    return count


# returns the length of the longest common extension with a character and their complimentary character
# starting at string[n1] and reverse string[n2]
def lce_query_comp_even(length, string, str_reverse, n1, n2, comp_dict):
    count = 0
    while n1 + count < length and n2 + count < length \
            and (string[n1 + count] in compare_complimentary.query_comp(str_reverse[n2 + count], comp_dict)):
        count += 1
    return count


# the center of an odd palindrome can be
def lce_query_comp_odd(length, string, str_reverse, n1, n2, comp_dict):
    count = 1
    while n1 + count < length and n2 + count < length \
            and (string[n1 + count] in compare_complimentary.query_comp(str_reverse[n2 + count], comp_dict)):
        count += 1
    return count


# will iterate through the string and the reverse of the string to find at longest common extensions 
# for even palindromes it is string [q + 1] and the reverse string [length - q - 1 ]and 
# for odd palindromes it is string [q] and the reverse string [length - q - 1 ]and 
def lce_queries(length, string, str_reverse, comp_dict):
    lce_odd = []
    lce_even = []
    if bool(comp_dict):
        for q in range(length):
            lce_even.append(lce_query_comp_even(length, string, str_reverse, q + 1, length - q - 1, comp_dict))
            lce_odd.append(lce_query_comp_odd(length, string, str_reverse, q, length - q - 1, comp_dict))
    else:
        for q in range(length):
            lce_even.append(lce_query(length, string, str_reverse, q + 1, length - q - 1))
            lce_odd.append(lce_query(length, string, str_reverse, q, length - q - 1))
    return lce_even, lce_odd


# Returns the even and odd longest common extension between the string and the reverse of the string
def lce(string, comp_dict):
    length = len(string)
    str_reverse = string[::-1]
    return lce_queries(length, string, str_reverse, comp_dict)
