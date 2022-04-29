# Returns the List U where U is the start positions of maximal palindromes is stored at the end position
def u(mpl):
    u_list = []
    for i in range(len(mpl)):
        u_i = []
        for j in range(len(mpl[i])):
            u_i.insert(0, i + 1 - mpl[i][j])
        u_list.append(u_i)
    return u_list
