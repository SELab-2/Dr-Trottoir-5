from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import TrashContainerListCreateView
from pickupdays.models import PickUpDay
from users.models import User
from ronde.models import Building
from model_bakery import baker


class TrashContainerTestCase(APITestCase):
    """
        Test if the trashcontainer model behaves as intended
    """

    def setUp(self):
        pickupDay = baker.make(PickUpDay, start_hour="12:00", end_hour="13:00")
        building = baker.make(Building)
        self.containerData = {"type": "PM", "collection_days": [pickupDay.id], "building": building.id}
        self.user = User.objects.create(role="SU")

    def testAddContainer(self):
        """
            Test if we can add a trash container
        """
        factory = APIRequestFactory()
        request = factory.post("/api/containers/", self.containerData)
        force_authenticate(request, user=self.user)
        response = TrashContainerListCreateView.as_view()(request).data
        days = response["collection_days_detail"]
        self.assertEqual(response["type"], "PM")
        self.assertEqual(len(days), 1)
        self.assertEqual(days[0]["start_hour"], "12:00:00")
        self.assertEqual(days[0]["end_hour"], "13:00:00")
