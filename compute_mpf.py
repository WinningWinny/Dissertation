import construct_graph


# Return lists of maximal palindrome created from the path found.
def construct_mpf(string, path):
    if path is None:
        return None
    s = ''.join(string)  # joins list of character to single string
    path.reverse()
    mpf_list = [s[path[i]:path[i + 1]] for i in range(len(path) - 1)]  # breaks string into maximal palindrome list
    return mpf_list


# Return lists of maximal palindrome factorisation that is equivalent to the string made up of prefix palindrome &
# the rest of the string and returns 0 if there is not one
def mpf_pp(string, path_dic, pp):
    mpf_list = []
    for j in range(len(pp)):
        path = construct_graph.point_to_point(pp[j], len(string), path_dic)
        if path is not None:
            pp_list = construct_mpf(string, path)
            pp_list.insert(0, string[:pp[j]])
            mpf_list.append(pp_list)
    return mpf_list


# Return lists of maximal palindrome factorisation that is equivalent to the string made up of the suffix palindrome &
# the rest of the string and returns 0 if there is not one
def mpf_sp(string, path_dic, sp):
    mpf_list = []
    for i in range(len(sp)):
        path = construct_graph.point_to_point(0, sp[i], path_dic)
        if path is not None:
            sp_list = construct_mpf(string, path)
            sp_list.append(string[sp[i]:])
            mpf_list.append(sp_list)
    return mpf_list


# Return lists of maximal palindromes that is equivalent to the string made up of the prefix palindrome &
# suffix palindrome & the rest of the string and returns 0 if there is not one
def mpf_pp_sp(string, path_dic, pp, sp):
    mpf_list = []
    for i in range(len(sp)):
        for j in range(len(pp)):
            if not (pp[j] >= sp[i]):
                path = construct_graph.point_to_point(pp[j], sp[i], path_dic)
                if path is not None:
                    sp_pp_list = construct_mpf(string, path)
                    sp_pp_list.append(string[sp[i]:])
                    sp_pp_list.insert(0, string[:pp[j]])
                    mpf_list.append(sp_pp_list)
    return mpf_list


# returns the shortest maximal palindrome factorisation
# that is equivalent to the string and returns 0 if there is not one
def mpf(string, path_dic):
    path = construct_graph.point_to_point(0, len(string), path_dic)
    return construct_mpf(string, path)
