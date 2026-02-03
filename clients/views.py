from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
def client_list(request):
    clients = Client.objects.all()
    status = request.query_params.get('status')
    if status:
        clients = clients.filter(status=status)
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
