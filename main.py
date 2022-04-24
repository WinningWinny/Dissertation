import compute_initial_pal
import compute_mp_mpl
import compute_mpf
import compute_pp_sp
import compute_u
import construct_graph
import test_set
import time


# return the output of the list MPF or None is there is not one
def find_mpf(string, comp_dict):
    mp, mpl = compute_mp_mpl.mp_mpl(string, comp_dict)  # finds the list MP(s) and MPL(s)
    u = compute_u.u(mpl)  # find the list u(s)
    pp = compute_pp_sp.pp(mp)
    sp = compute_pp_sp.sp(mp)
    graph = construct_graph.construct_graph(u)
    path_dic = construct_graph.bfs(graph)
    mpf = compute_mpf.mpf(string, path_dic)
    return mpf


if __name__ == '__main__':
    start_time = time.time()
    for i in range(len(test_set.test_data)):
        print(find_mpf(test_set.test_data[i], {}))
    for i in range(len(test_set.dna_set)):
        print(find_mpf(test_set.dna_set[i], test_set.dna_rna_comp_dict))

    print("--- %s seconds ---" % (time.time() - start_time))
