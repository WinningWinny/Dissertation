import compute_lce


# creates the list mp from even and odd lce
# and will create the list mpl in parallel
# will keep any even lce greater than 0 and any odd lce greater than 1,
# will keep maximal palindrome of 1 if there is no other
def mp_mpl(string, comp_dict):
    lce_even, lce_odd = compute_lce.lce(string, comp_dict)
    n = len(lce_odd)
    mp_list = []  # Construct the empty list MP
    mpl_list = [[] for i in range(len(string))]  # Construct the empty list MPL
    for i in range(n):
        x = lce_even[i] * 2
        y = (lce_odd[i] * 2) - 1
        mp_i = []  # store MP[i]
        if x != 0:
            if y != 1:
                mp_i.append(y)
                mpl_list[i + lce_odd[i] - 1].append(y)
            mp_i.append(x)
            mpl_list[i + lce_even[i]].append(x)
        else:
            mp_i.append(y)
            mpl_list[i + lce_odd[i] - 1].append(y)
        mp_list.append(mp_i)
    return mp_list, mpl_list
