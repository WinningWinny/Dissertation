# return the complimentary characters
def query_comp(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return []


# create a complimentary dictionary from 2d list
def create_comp_dict(compliments):
    dicts = {}
    for i in range(len(compliments)):
        for j in range(len(compliments[i])):
            dicts[compliments[i]] = compliments[j]
    return dicts


def test_comp(x1, x2, dictionary):
    return x2 in query_comp(x1, dictionary)
