from django.contrib.auth.models import User, Group
from models import Country, UserFamily, UserProfile, UserActivity
from rest_framework import serializers
from django.conf import settings

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'country', 'family')
        depth = 1

class UserFamilySerializer(serializers.HyperlinkedModelSerializer):
    members = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = UserFamily
        fields = ('id', 'family_name', 'members')

class UserActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('id', 'user', 'browser', 'os', 'action', 'date')
        depth = 2

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
