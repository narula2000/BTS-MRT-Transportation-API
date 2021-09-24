from api.models import Station
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .graph import Graph


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Find Route by Name': '/find_route_name',
        'Find Route by ID': '/find_route_id',
        'Get Station Name by ID': '/get_station_name',
        'Get Station ID by Name': '/get_station_id'
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
        graph = Graph()
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
        graph = Graph()
        path = graph.dfsById(station_source_id, station_destination_id)
        return Response(path if path != -1 else [])


@api_view(['GET', 'POST'])
def getStationNameById(request):
    if request.method == 'GET':
        api_info_id = {
            "station_id": "ID of either MRT or BTS starting station i.e. N08",
        }
        return Response(api_info_id)
    elif request.method == 'POST':
        data = request.data
        try:
            station_id = data["station_id"]
        except KeyError:
            raise ParseError("Wrong Key Received")
        try:
            station = Station.objects.get(station_id=station_id)
        except Station.DoesNotExist:
            raise ParseError("%s: This id doesn't exist." %
                             (station_id))
        return Response(station.station_name)


@api_view(['GET', 'POST'])
def getStationIdByName(request):
    if request.method == 'GET':
        api_info_id = {
            "station_name": "Name of either MRT or BTS starting station i.e. Mo_Chit"
        }
        return Response(api_info_id)
    elif request.method == 'POST':
        data = request.data
        try:
            station_name = data["station_name"]
        except KeyError:
            raise ParseError("Wrong Key Received")
        try:
            station = Station.objects.get(station_name=station_name)
        except Station.DoesNotExist:
            raise ParseError("%s: This station doesn't exist. You might forget _" % (
                station_name))
        return Response(station.station_id)
