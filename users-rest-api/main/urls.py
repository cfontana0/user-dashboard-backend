from django.conf.urls import url, include
from rest_framework import routers
from users import views
from django.contrib import admin
from rest_framework.authtoken import views as viewRest
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'profile', views.UserProfileViewSet)
router.register(r'activity', views.UserActivityViewSet)
router.register(r'family', views.UserFamilyViewSet)
router.register(r'country', views.CountryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^authenticate/', viewRest.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
