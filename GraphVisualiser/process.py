# created by me
from . import simulation
import os


def simulateGraph(request):
    """
    This will return a tuple
    1. valid graph
    2. message
    3. number of stages in the graph
    """
    ALGOS = ["dfs", "bfs", "dijkstra", "kruskal", "prim"] 
    numberofnodes = request.GET.get('nodes', '')
    algo = request.GET.get('algo', '').lower()
    try:
        numberofnodes = int(numberofnodes) # checking if the user has not entered a string in the input
    except:
        return False, "Invalid number of nodes", -1

    if (numberofnodes == 0):
        return False, "Nodes can't be zero.", -1

    if (algo not in ALGOS): return False, "Invalid Algo", -1  # if the user has not entered the algos from the given placeholder

    givenEdgeString = request.GET.get('edges', '').strip()
    givenEdgeStrings = givenEdgeString.split("\r\n")
    if (givenEdgeStrings[0] == ''): givenEdgeStrings = []  # storing the edges in the list

    g = [] # this will store edges

    nodes = list(range(1, numberofnodes + 1))
    print(givenEdgeStrings)
    print(nodes)
    for R in givenEdgeStrings:
        try:
            x = list(map(int, R.split()))
            if (len(x) == 2):
                if (algo not in ["dfs", "bfs"]): return False, "Invalid Edges", -1  # checking if the length is 2 then the given algo can't be djikstra etc.
                u, v = x
                if (not u in nodes) or (not v in nodes): return False, "Invalid Edges", -1
                g.append(x)
            elif (len(x) == 3):
                if algo in ["dfs", "bfs"]: return False, "Invalid Edges", -1  # checking if the length is 3 then the given algo can't be dfs, bfs.
                u, v, w = x
                if (algo == "dijkstra") and w < 0: return False, "Dijkstra can't handle negative edge weights.", -1
                if (not u in nodes) or (not v in nodes): return False, "Invalid Edges", -1
                g.append(x)
            else:
                return False, "Invalid Edges", -1
        except:
            return False, "Invalid Edges", -1


    # clearing all the files inside output before running the function
    dir = 'static/output'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


    return True, None, simulation.start(g, numberofnodes, algo.lower())
