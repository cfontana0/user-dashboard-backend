from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.serializers import UserSerializer, GroupSerializer, UserActivitySerializer, CountrySerializer, UserFamilySerializer, UserProfileSerializer
from models import Country, UserFamily, UserProfile, UserActivity

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class UserFamilyViewSet(viewsets.ModelViewSet):
    queryset = UserFamily.objects.all()
    serializer_class = UserFamilySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer


