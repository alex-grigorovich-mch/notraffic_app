from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.notraffic.views import IntersectionViewSet

router = DefaultRouter()

router.register("notraffic", IntersectionViewSet, basename="api-v1-notraffic")

urlpatterns = [
    path("", include(router.urls)),
]
