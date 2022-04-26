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
    pp = compute_pp_sp.pp(mp)
    sp = compute_pp_sp.sp(mp)
    u = compute_u.u(mpl)  # find the list u(s)
    graph = construct_graph.construct_graph(u)
    path_dic = construct_graph.bfs(graph)
    mpf = compute_mpf.mpf(string, path_dic)
    print("MP    ", mp)
    print("PP    ", pp)
    print("SP    ", sp)
    print("MPL   ", mpl)
    print("U     ", u)
    print("Graph ", graph)
    print("Path Dictionary", path_dic)
    return mpf


if __name__ == '__main__':
    start_time = time.time()
    for i in range(len(test_set.user_data)):
        print(find_mpf(test_set.user_data[i],  test_set.user_comp_dict))
    print("--- %s seconds ---" % (time.time() - start_time))
