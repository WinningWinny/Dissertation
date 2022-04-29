# Finds the smallest initial odd greater than 1 and even palindrome and add them to a list,
# if no  odd greater than 1 or even palindrome is found then we add a palindrome equal to 1
# the function will remove the palindrome at the front of the string and will continue until the string is empty
def initial_palindrome(d):
    current_list = d
    done = False
    mp = []
    index = 0
    while len(current_list) > 0 and not done:
        even_index = pal_even(current_list, len(current_list))
        odd_index = pal_odd(current_list, len(current_list))
        if even_index == 0 and odd_index == 0:
            current_list = current_list[1:]
            index += 1
        else:
            if even_index != 0:
                current_list = current_list[even_index:]
                index += even_index
            else:
                current_list = current_list[odd_index:]
                index += odd_index
        mp.append(index)
    return mp


# Finding initial even palindrome
# difference from pal_odd as have n-1 palindrome center for m 
def pal_even(d, n):
    enp = 0
    pal = 0
    m = [-1] * (n - 1)
    pal, done, enp, m = l1_even(pal, d, n, enp, m)
    return pal


# difference from l1_odd that the value of bp is enp - 1
def l1_even(pal, d, n, enp, m):
    done = False
    enp += 1
    if enp == n:
        done = True
    else:
        mdp = bp = enp - 1
        count = 0
        pal, count, enp, mdp, bp, m, done = l2(pal, d, n, count, enp, mdp, bp, m, done)
    if not done:
        return l1_even(pal, d, n, enp, m)
    return pal, done, enp, m


# Finding initial odd palindrome greater than 1
# difference from pal_odd as have n palindrome center for m 
def pal_odd(d, n):
    enp = 0
    pal = 0
    m = [-1] * (n - 1)
    pal, done, enp, m = l1_odd(pal, d, n, enp, m)
    return pal


# the difference from l1_even that the value of bp is enp -
def l1_odd(pal, d, n, enp, m):
    done = False
    enp += 1
    if enp == n:
        done = True
    if not done:
        bp = enp
        mdp = enp - 1
        count = 0
        pal, count, enp, mdp, bp, m, done = l2(pal, d, n, count, enp, mdp, bp, m, done)
    else:
        return pal, done, enp, m
    if not done:
        pal, done, enp, m = l1_odd(pal, d, n, enp, m)
    return pal, done, enp, m


def l2(pal, d, n, count, enp, mdp, bp, m, done):
    while d[enp] == d[bp]:
        count += 1
        enp += 1
        bp -= 1
        if bp == -1:
            return enp, count, enp, mdp, bp, m, True
        if enp == n:
            return pal, count, enp, mdp, bp, m, True
    m[mdp] = count
    for f in range(1, count + 1):
        if m[mdp - f] != count - f:
            m[mdp + f] = min(count - f, m[mdp - f])
        else:
            mdp = mdp + f
            count = count - f
            bp = mdp - count
            return l2(pal, d, n, count, enp, mdp, bp, m, done)
    return pal, count, enp, mdp, bp, m, done
