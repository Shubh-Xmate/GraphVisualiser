import requests, zipfile
from io import BytesIO
import os

################################ Main where some algo starts #############################


def start(g, nodes, algo):
    """
    This will channel graph and nodes to different functions
    based on the algo used and then generate the images which
    will help me create the animation.
    """

    dir = '/Users/vaibhavgoyal/Documents/Programming/Python/PycharmProjects/GraphVisualiserRecievesImages/static/output'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    # importing necessary modules
    print('Downloading started')

    # Defining the zip file URL
    url = 'http://127.0.0.1:8000/solve'

    edges = ""
    for e in g:
        s = ' '.join([str(n) for n in e])
        edges += s + '\n'
    print(edges, nodes, algo)

    payload = {"nodes": nodes, "algo": algo, "edges": edges}

    # Downloading the file by sending the request to the URL
    req = requests.get(url, params=payload)
    print('Downloading Completed')

    # extracting the zip file contents
    zfile = zipfile.ZipFile(BytesIO(req.content))
    zfile.extractall('/Users/vaibhavgoyal/Documents/Programming/Python/PycharmProjects/GraphVisualiserRecievesImages/static/output')
    return 5


g = [[1, 2, 1], [1, 3, 2], [2, 3, 4], [3, 4, 3], [4, 5, 2]]
nodes = 5
start(g, nodes, "dijkstra")
