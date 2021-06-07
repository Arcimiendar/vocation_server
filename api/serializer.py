from rest_framework import serializers
from api.models import SearchWord


class SearchWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchWord
        fields = '__all__'
