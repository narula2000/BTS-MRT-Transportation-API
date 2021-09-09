from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'Find Route': '/find_route',
        'Can Reach': '/can_reach',
        'All Routes': '/all_routes'
    }
    return Response(api_urls)
