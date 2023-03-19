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
        pickupDay1 = baker.make(PickUpDay, start_hour="12:00", end_hour="13:00")
        pickupDay2 = baker.make(PickUpDay, start_hour="15:00", end_hour="15:30")
        building = baker.make(Building)
        self.containerData = {"type": "PM", "collection_days": [pickupDay1.id, pickupDay2.id], "building": building.id}
        self.containerData2 = {"type": "PM", "collection_days": [pickupDay2.id, pickupDay1.id], "building": building.id}
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
        self.assertEqual(len(days), 2)
        self.assertEqual(days[0]["start_hour"], "12:00:00")
        self.assertEqual(days[0]["end_hour"], "13:00:00")

    def testAddSameContainers(self):
        """
            Make sure that duplicate trash containers are not stored twice in database
        """
        factory = APIRequestFactory()
        request = factory.post("/api/containers/", self.containerData)
        force_authenticate(request, user=self.user)
        id1 = TrashContainerListCreateView.as_view()(request).data["id"]

        request2 = factory.post("/api/containers/", self.containerData2)
        force_authenticate(request2, user=self.user)
        id2 = TrashContainerListCreateView.as_view()(request2).data["id"]
        self.assertEqual(id1, id2)
