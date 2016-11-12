from rest_framework import routers, serializers, viewsets
from .models import Issues, SubCategory, Category


class IssuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'