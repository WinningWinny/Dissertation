test_data = ["010abba00100","abbcbbcbbbcbb",
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
             ("ababa123321,.,.,yty[{1kjoppojk21}]975313579" * 100),("qwertyuioplkjhgfdsazxcvbnmmnbvcxzasdfghjklpoiuytrewq"*1000)]



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

"""
for i in range(len(test_set.test_data)):
    pal = compute_initial_pal.palindrome(test_data[i])
    mp, mpl = compute_mp.mp(test_data[i])
    U = compute_u.u(mpl)
    PP = compute_pp_sp.pp(mp)
    SP = compute_pp_sp.sp(mp)
    graph = construct_graph.construct_graph(U)
    path_dic = construct_graph.bfs(graph)
    path = construct_graph.point_to_point(0, len(test_data[i]), path_dic)
    mpf = compute_mpf.mpf(test_data[i], path)
    mpflistpp = compute_mpf.mpfpp(test_data[i], path_dic, PP)
    mpflistsp = compute_mpf.mpfsp(test_data[i], path_dic, SP)
    mpflistppsp = compute_mpf.mpfppsp(test_data[i], path_dic, PP, SP)
    print("---word", test_data[i], len(test_data[i]))
    print("pal    ", pal)
    print("mps    ", mp)
    print("mpl    ", mpl)
    print("U      ", U)
    print("PP     ", PP)
    print("SP     ", SP)
    print("Graph  ", graph)
    print("path_dic", path_dic)
    print("path   ", path)
    print("MPF    ", mpf)
    print("MPFpp  ", mpflistpp)
    print("MPFsp  ", mpflistsp)
    print("MPFppsp", mpflistppsp)

    print(len(test_data[i]), construct_graph.point_to_point(0, len(test_data[i]), path_dic))
    if construct_graph.point_to_point(0, len(test_data[i]), path_dic) != None:
        s = ''.join(test_data[i])
        maxPalindromes = list(map(int, construct_graph.point_to_point(0, len(test_data[i]), path_dic)))
        maxPalindromes.reverse()
        mpf = [s[maxPalindromes[i]:maxPalindromes[i + 1]] for i in range(len(maxPalindromes) - 1)]
        print(mpf)
    for k in range(0, len(test_data[i]) + 1):
        for j in range(k, len(test_data[i]) + 1):
            if construct_graph.point_to_point(k, j, path_dic) != None:
                # print(k, j, construct_graph.pointToPoint(k, j, path_dic))
                pass
    print(''.join(test_data[i]))
for i in range(len(test_data)):
    print(''.join(test_data[i]))
    print(find_mpf(test_data[i]))
    
    """
