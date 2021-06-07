from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from api.serializer import SearchWordSerializer
from api.models import SearchWord


class ListCreateSearchWordView(ListCreateAPIView):
    queryset = SearchWord.objects.all()
    serializer_class = SearchWordSerializer


class DestroySearchWordView(DestroyAPIView):
    serializer_class = SearchWordSerializer
    queryset = SearchWord.objects.all()
