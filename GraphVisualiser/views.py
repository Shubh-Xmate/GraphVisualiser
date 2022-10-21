# created by me
from django.http import HttpResponse
from django.shortcuts import render
from . import process


def index(request):
    return render(request, 'index.html')


def solve(request):
    # is request se data utha sakte hai form ka
    # print(request.GET.get('givenMatrix', 'default')) : jis element ka naam text hai request mai uska data utha lega
    valid, message, solution = process.simulateGraph(request)
    if (valid == False):
        params = {"message": message}
        return render(request, "invalid.html", params)
    else:
        algo = request.GET.get("algo").upper()
        params = {"stages": solution, "algo": algo}
        # here I have to process the images which are formed
        if (algo == "DIJKSTRA") :
            print("dijskstra rendered")
            return render(request, "dijkstra.html", params)
        return render(request, "DFSBFSPrimKruskal.html", params)
