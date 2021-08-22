from django.contrib.auth.models import User, Group
from rest_framework import serializers

from endpoints.models import PropertyType, State, City, Category, Transation, Property, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'slug']


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'image', 'city', 'price',
                  'category', 'sqft', 'baths', 'beds']


class TransationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transation
        fields = ['id', 'slug', 'propertyTypes']


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'slug', 'state', 'zip']


class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'slug']


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'slug']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'feedback', 'rating', 'avatar']
