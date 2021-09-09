from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TrainSerializers
from .models import Train


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
    serialize = TrainSerializers(train, many=True)
    return Response(serialize.data)
