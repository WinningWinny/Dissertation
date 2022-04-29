# return the complimentary characters
def query_comp(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return []


def test_comp(x1, x2, dictionary):
    return x2 in query_comp(x1, dictionary)
