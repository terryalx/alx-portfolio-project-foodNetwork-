from rest_framework import viewsets
# from ..webapp.models import all_resturant
from webapp.models import all_resturant

from .serializers import AllModelSerializer

class ListModelViewSet(viewsets.ModelViewSet):
    queryset = all_resturant.objects.all()
    serializer_class = AllModelSerializer
