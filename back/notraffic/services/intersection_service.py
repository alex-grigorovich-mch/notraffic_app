from dataclasses import dataclass
from decimal import Decimal

from notraffic.models import Intersection, Street


@dataclass(frozen=True)
class IntersectionService:
    name: str
    latitude: Decimal
    longitude: Decimal
    first_street: str
    second_street: str

    def create_intersection(self) -> Intersection:
        """
        Implemented for the case if first or second street does not exist.
        """

        first_street, _ = Street.objects.get_or_create(name=self.first_street)
        second_street, _ = Street.objects.get_or_create(name=self.second_street)

        return Intersection.objects.create(
            name=self.name,
            latitude=self.latitude,
            longitude=self.longitude,
            first_street=first_street,
            second_street=second_street,
        )

    def udpate_intersection(self, intersection) -> Intersection:
        """
        Implemented for the case if first or second street does not exist.
        """

        first_street, _ = Street.objects.get_or_create(name=self.first_street)
        second_street, _ = Street.objects.get_or_create(name=self.second_street)
        intersection.name = self.name
        intersection.latitude = self.latitude
        intersection.longitude = self.longitude
        intersection.first_street = first_street
        intersection.second_street = second_street

        intersection.save()
        return intersection
