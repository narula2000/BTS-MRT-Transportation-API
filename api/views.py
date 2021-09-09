from rest_framework.decorators import api_view
from rest_framework.response import Response
from .graph import Graph


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Find Route': '/find_route',
        'Can Reach': '/can_reach'
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def findRoute(request):
    if request.method == 'GET':
        api_info = {
            "station_source": "Name of either MRT or BTS starting station i.e. Mo Chit",
            "station_destination": "Name of either MRT or BTS destination station i.e. Ekkamai"
        }
        return Response(api_info)
    elif request.method == 'POST':
        data = request.data
        graph = Graph()
        path = graph.dfs(data["station_source"], data["station_destination"])
        return Response(path if path != -1 else [])


@api_view(['GET', 'POST'])
def canReach(request):
    if request.method == 'GET':
        api_info = {
            "station_source": "Name of either MRT or BTS starting station i.e. Mo Chit",
            "station_destination": "Name of either MRT or BTS destination station i.e. Ekkamai"
        }
        return Response(api_info)
    elif request.method == 'POST':
        data = request.data
        graph = Graph()
        path = graph.dfs(data["station_source"], data["station_destination"])
        return Response(path != -1)
