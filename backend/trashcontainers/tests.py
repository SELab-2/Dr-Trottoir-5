from rest_framework.test import APITestCase, APIRequestFactory
from .views import TrashContainerListCreateView
from pickupdays.views import PickUpListCreateView


class TrashContainerTestCase(APITestCase):
    """
        Test if the trashcontainer model behaves as intended
    """

    def setUp(self):
        self.pickupdayData = {"day": "MO", "start_hour": "12:00", "end_hour": "13:00"}
        self.containerData = {"type": "PM", "collection_days": []}

    def testAddContainer(self):
        """
            Test if we can add a trash container
        """
        factory = APIRequestFactory()
        pickup_request = factory.post("/api/pickupday/", self.pickupdayData)
        pickup_response = PickUpListCreateView.as_view()(pickup_request).data

        self.containerData["collection_days"].append(pickup_response["id"])
        request = factory.post("/api/containers/", self.containerData)
        response = TrashContainerListCreateView.as_view()(request).data
        days = response["collection_days_detail"]
        self.assertEqual(response["type"], "PM")
        self.assertEqual(len(days), 1)
        self.assertEqual(days[0]["start_hour"], "12:00:00")
        self.assertEqual(days[0]["end_hour"], "13:00:00")
