# Returns list of the end positions of prefix palindromes
def pp(mp):
    pp_list = []
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            if i - (int((mp[i][j] - 1) / 2)) == 0:
                pp_list.append(mp[i][j])
    return pp_list


# Returns list of the start positions of suffix palindromes
def sp(mp):
    sp_list = []
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            if i + int(mp[i][j] / 2) == len(mp) - 1:
                sp_list.append(len(mp) - mp[i][j])
    return sp_list
