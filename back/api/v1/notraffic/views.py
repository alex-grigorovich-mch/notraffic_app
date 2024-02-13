from django.db.models import Model
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
from rest_framework.serializers import Serializer

from api.v1.notraffic.serializers import (
    CreateIntersectionSerializer,
    ListGetIntersectionSerializer,
    UpdateIntersectionSerializer,
)
from common.viewset import (
    SeparateRequestAndResponseSerializerCreateModelMixin,
    SeparateRequestAndResponseSerializerListModelMixin,
    SeparateRequestAndResponseSerializersGenericViewSet,
    SeparateRequestAndResponseSerializerUpdateModelMixin,
)
from notraffic.models import Intersection
from notraffic.services.intersection_service import IntersectionService


class IntersectionViewSet(
    SeparateRequestAndResponseSerializerCreateModelMixin,
    SeparateRequestAndResponseSerializerListModelMixin,
    SeparateRequestAndResponseSerializerUpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    SeparateRequestAndResponseSerializersGenericViewSet,
):
    queryset = Intersection.objects.all()

    request_serializers_by_action = {
        "create": CreateIntersectionSerializer,
        "update": UpdateIntersectionSerializer,
        "retrieve": ListGetIntersectionSerializer,
    }

    response_serializers_by_action = {
        "create": ListGetIntersectionSerializer,
        "list": ListGetIntersectionSerializer,
        "update": ListGetIntersectionSerializer,
        "retrieve": ListGetIntersectionSerializer,
    }

    def perform_create(self, serializer: Serializer) -> Model:
        return IntersectionService(**serializer.validated_data).create_intersection()

    def perform_update(self, serializer: Serializer):

        intersection = self.get_object()
        return IntersectionService(**serializer.validated_data).udpate_intersection(intersection)
