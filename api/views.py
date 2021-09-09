from .models import Train
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StationSerializers, TrainSerializers, Train_to_StationSerializers


@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'Find Route': '/find_route',
        'Can Reach': '/can_reach',
        'All Routes': '/all_routes'
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def allRoutes(req):
    train = Train.objects.all()
    serializers = TrainSerializers(train)
    return Response(serializers.data)