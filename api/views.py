from rest_framework.decorators import api_view
from rest_framework.response import Response
from .graph import Graph


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Find Route': '/find_route'
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def findRouteByName(request):
    if request.method == 'GET':
        api_info_name = {
            "station_source": "Name of either MRT or BTS starting station i.e. Mo_Chit",
            "station_destination": "Name of either MRT or BTS destination station i.e. Ekkamai"
        }
        return Response(api_info_name)
    elif request.method == 'POST':
        data = request.data
        graph = Graph()
        path = graph.dfsByName(data["station_source"], data["station_destination"])
        return Response(path if path != -1 else [])


@api_view(['GET', 'POST'])
def findRouteById(request):
    if request.method == 'GET':
        api_info_id = {
            "station_source_id": "ID of either MRT or BTS starting station i.e. N08",
            "station_destination_id": "ID of either MRT or BTS destination station i.e. E07"
        }
        return Response(api_info_id)
    elif request.method == 'POST':
        data = request.data
        graph = Graph()
        path = graph.dfsById(data["station_source_id"], data["station_destination_id"])
        return Response(path if path != -1 else [])
