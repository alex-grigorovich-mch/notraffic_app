import pytest
from django.urls import reverse
from rest_framework import status

from notraffic.models import Intersection, Street


@pytest.mark.django_db
class TestNoTrafficAPI:
    @pytest.fixture
    def street1(self):
        return Street.objects.create(name="First Street")

    @pytest.fixture
    def street2(self):
        return Street.objects.create(name="Second Street")

    @pytest.fixture
    def intersection(self, street1, street2):
        return Intersection.objects.create(
            name="Test Intersection",
            latitude=40.7128,
            longitude=-74.0060,
            first_street=street1,
            second_street=street2,
        )

    @pytest.fixture
    def valid_payload_main_intersection_different_name(self, street1, street2):
        return {
            "name": "New Intersection",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "first_street": street1.name,
            "second_street": street2.name,
        }

    @pytest.fixture
    def valid_payload(self, street1, street2):
        return {
            "name": "New Intersection",
            "latitude": 42.3601,
            "longitude": -71.0589,
            "first_street": street1.name,
            "second_street": street2.name,
        }

    @pytest.fixture
    def valid_payload_if_no_streets_exist(self):
        return {
            "name": "New Intersection",
            "latitude": 42.3601,
            "longitude": -71.0589,
            "first_street": "first_test_street",
            "second_street": "second_test_street",
        }

    @pytest.fixture
    def invalid_payload(self, street1, street2):
        return {
            "name": "New Intersection",
            "longitude": -71.0589,
            "first_street": street1.name,
            "second_street": street2.name,
        }

    def test_list_intersections(self, api_client, intersection):
        url = reverse("api-v1-notraffic-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert Intersection.objects.count() == 1

    def test_create_intersection(self, api_client, valid_payload):
        url = reverse("api-v1-notraffic-list")
        response = api_client.post(url, valid_payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Intersection.objects.count() == 1

    def test_create_intersection_streets_if_no_streets_exist(self, api_client, valid_payload_if_no_streets_exist):
        url = reverse("api-v1-notraffic-list")
        response = api_client.post(url, valid_payload_if_no_streets_exist, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Intersection.objects.count() == 1
        assert Street.objects.get(name="first_test_street").name == valid_payload_if_no_streets_exist['first_street']
        assert Street.objects.get(name="second_test_street").name == valid_payload_if_no_streets_exist['second_street']

    def test_create_intersection_with_same_coordinates_and_streets(
        self, api_client, intersection, valid_payload_main_intersection_different_name
    ):
        url = reverse("api-v1-notraffic-list")
        response = api_client.post(url, valid_payload_main_intersection_different_name, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Intersection.objects.count() == 1

    def test_retrieve_intersection(self, api_client, intersection):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Test Intersection"

    def test_update_intersection(self, api_client, intersection, valid_payload):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        response = api_client.put(url, valid_payload, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Intersection.objects.get(pk=intersection.pk).name == valid_payload["name"]

    def test_update_intersection_streets_if_no_streets_exist(
        self, api_client, intersection, valid_payload_if_no_streets_exist
    ):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        response = api_client.put(url, valid_payload_if_no_streets_exist, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Street.objects.get(name="first_test_street").name == valid_payload_if_no_streets_exist['first_street']
        assert Street.objects.get(name="second_test_street").name == valid_payload_if_no_streets_exist['second_street']

    def test_delete_intersection(self, api_client, intersection):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Intersection.objects.count() == 0

    def test_create_intersection_invalid_payload(self, api_client, invalid_payload):
        url = reverse("api-v1-notraffic-list")
        response = api_client.post(url, invalid_payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Intersection.objects.count() == 0

    def test_create_intersection_same_streets(self, api_client, street1):
        url = reverse("api-v1-notraffic-list")
        payload = {
            "name": "New Intersection",
            "latitude": 42.3601,
            "longitude": -71.0589,
            "first_street": street1.name,
            "second_street": street1.name,  # Same street as first_street
        }
        response = api_client.post(url, payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Intersection.objects.count() == 0

    def test_update_intersection_invalid_payload(self, api_client, intersection, invalid_payload):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        response = api_client.put(url, invalid_payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Intersection.objects.get(pk=intersection.pk) == intersection

    def test_update_intersection_same_streets(self, api_client, intersection, street1):
        url = reverse("api-v1-notraffic-detail", kwargs={"pk": intersection.pk})
        payload = {
            "name": "Updated Intersection",
            "latitude": 45.5051,
            "longitude": -122.6750,
            "first_street": street1.name,
            "second_street": street1.name,  # Same street as first_street
        }
        response = api_client.put(url, payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Intersection.objects.get(pk=intersection.pk) == intersection
