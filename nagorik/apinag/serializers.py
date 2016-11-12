from rest_framework import routers, serializers, viewsets
from .models import Issues, SubCategory, Category
from django.contrib.auth.models import User, Group


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
