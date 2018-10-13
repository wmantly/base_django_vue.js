from django.conf.urls import url, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.TeamSet)


urlpatterns = [
    url(r'api/^', include(router.urls)),
    url(r'api/accounts/', include('rest_registration.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
