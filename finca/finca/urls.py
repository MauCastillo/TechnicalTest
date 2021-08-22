from django.urls import include, path
from rest_framework import routers
from endpoints import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'properties', views.PropertySerializerViewSet)
router.register(r'categories', views.CategorySerializerViewSet)
router.register(r'cities', views.CitySerializerViewSet)
router.register(r'states', views.StateSerializerViewSet)
router.register(r'propertyTypes', views.PropertyTypeSerializerViewSet)
router.register(r'transactions', views.TransationSerializerViewSet)
router.register(r'reviews', views.ReviewSerializerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
