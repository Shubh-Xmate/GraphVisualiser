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

    # importing necessary modules
    print('Downloading started')

    # Defining the zip file URL
    url = 'https://graphimages.herokuapp.com/solve'
    # url = 'http://localhost:8080/solve'

    # Split URL to get the file name
    filename = url.split('/')[-1]

    edges = ""
    for e in g:
        s = ' '.join([str(n) for n in e])
        edges += s + '\n'
    print(edges)
    print(nodes, algo)

    payload = {"nodes": nodes, "algo": algo, "edges": edges}

    # Downloading the file by sending the request to the URL
    req = requests.get(url, params=payload)
    print('Downloading Completed')
    print(req.content)
    # extracting the zip file contents
    zfile = zipfile.ZipFile(BytesIO(req.content))
    zfile.extractall('static/output')

    # I have to return the number of images in the zip file
    path = 'static/output'
    images = len(os.listdir(path=path))
    if (algo == 'dijkstra'): return images / 2
    return images
