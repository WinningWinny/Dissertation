user_data = []
user_comp_dict = {}

test_data = ["010abba00100", "abbcbbcbbbcbb",
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
             "111001abcddcba01010", "0100100010101010", "abbbbacabbbbaaca",
             ("ababa123321,.,.,yty[{1kjoppojk21}]975313579" * 100),
             ("qwertyuioplkjhgfdsazxcvbnmmnbvcxzasdfghjklpoiuytrewq" * 1000)]

dna_set = ["AG",
           "ACG",
           "CCTU",
           "AGCUGA",
           ("CCTTTUGAGACU" * 1),
           ("AGCUGA" * 1),
           ("AGAGAGTUTCCCCCCUTU" * 1),
           "CAGTTGGAACAGG"
           ]

dna_rna_comp_dict = {
    "A": ["G"],
    "G": ["A"],
    "C": ["T", "U"],
    "T": ["C"],
    "U": ["C"]
}
