from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
def client_list(request):
    clients = Client.objects.all().order_by('id')
    status = request.query_params.get('status')
    if status:
        clients = clients.filter(status=status)
    paginator = PageNumberPagination()
    paginator.page_size_query_param = 'page_size'
    if 'page_size' in request.query_params:
        try:
            paginator.page_size = int(request.query_params['page_size'])
        except (TypeError, ValueError):
            pass
    page = paginator.paginate_queryset(clients, request)
    serializer = ClientSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)
