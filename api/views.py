from api.models import Station
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .graph import Graph


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Find Route by Name': '/find_route_name',
        'Find Route by ID': '/find_route_id'
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
        try:
            station_source_name = data["station_source"]
            station_destination_name = data["station_destination"]
        except KeyError:
            raise ParseError("Wrong Key Received")
        try:
            Station.objects.get(station_name=station_source_name)
        except Station.DoesNotExist:
            raise ParseError(
                "%s: This station doesn't exist. You might forget _" % (station_source_name))
        try:
            Station.objects.get(station_name=station_destination_name)
        except Station.DoesNotExist:
            raise ParseError("%s: This station doesn't exist. You might forget _" % (
                station_destination_name))
        path = graph.dfsByName(station_source_name, station_destination_name)
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
        try:
            station_source_id = data["station_source_id"]
            station_destination_id = data["station_destination_id"]
        except KeyError:
            raise ParseError("Wrong Key Received")
        try:
            Station.objects.get(station_id=station_source_id)
        except Station.DoesNotExist:
            raise ParseError("%s: This id doesn't exist." %
                             (station_source_id))
        try:
            Station.objects.get(station_id=station_destination_id)
        except Station.DoesNotExist:
            raise ParseError("%s: This id doesn't exist." %
                             (station_destination_id))
        path = graph.dfsById(station_source_id, station_destination_id)
        return Response(path if path != -1 else [])
