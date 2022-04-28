user_comp_dict = {}
user_data = []

test_data_multiple = [
    ("a" * 5),
    ("aba" * 5),
    ("bb" * 5),
    ("abba" * 5),
    ("abcd" * 5),
    ("abcddcba" * 5),
    ("0101001001001010" * 5),
    ("01010000" * 5),
    ("0111101011110000" * 5),
    ("010110101011110000" * 5),
    ("bbbbbbbbbb" * 5),
    ("abbacbbc" * 5),
    ("111000" * 5),
    ("abababababababababababababababababababababababababababababa" * 5),
    ("111000abcddcba0101" * 5),
    ("111001abcddcba01010" * 5),
    ("abbbbacabbbbaaca" * 5),
    ("ababa123321,.,.,yty[{1kjoppojk21}]975313579" * 50),
    ("qwertyuioplkjhgfdsazxcvbnmmnbvcxzasdfghjklpoiuytrewq" * 50)
]

test_data = [
    "010abba00100",
    "abbcbbcbbbcbb",
    "abbcbbcbbbcbbbbcbbbcbb",
    "a",
    "aba",
    "bb",
    "abba",
    "abcd",
    "abcddcba",
    "0110011100001100110000110010011010",
    "0101001001001010",
    "01010000",
    "0111101011110000",
    "010110101011110000",
    "abbcbbcbbbcbb",
    "bbbbbbbbbb",
    "abbacbbc",
    "111000",
    "01010abbcbbcbbbcbb0110",
    "111000abcddcba01010000abcd0111101011110000aba",
    "abababababababababababababababababababababababababababababa",
    "111000abcddcba0101",
    "111001abcddcba01010",
    "0100100010101010",
    "abbbbacabbbbaaca",
    ("ababa123321,.,.,yty[{1kjoppojk21}]975313579" * 10),
    ("qwertyuioplkjhgfdsazxcvbnmmnbvcxzasdfghjklpoiuytrewq" * 10)
]

test_data_concatenate = [''.join(test_data_multiple)]

dna_set = [
    "CATGTGGCCAATT"
]

dna_rna_comp_dict = {
    "A": ["T", "U"],
    "G": ["C"],
    "C": ["G"],
    "T": ["A"],
    "U": ["A"]
}
