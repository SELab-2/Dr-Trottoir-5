from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory
from .views import *
from .models import *


# Create your tests here.


class CreateTest(APITestCase):

    def setUp(self) -> None:
        self.wp = WeekPlanning.objects.create(week=0, year=2023).pk

    def testAddWeekPlanning(self):
        factory = APIRequestFactory()
        request = factory.post("/api/planning/weekplanning/", {"week": 12, "year": 2023})
        response = WeekPlanningCLAPIView.as_view()(request).data
        self.assertEqual(response["week"], 12)
        self.assertEqual(response["year"], 2023)
        self.assertIsNotNone(response["pk"])

    def testAddDagPlanning(self):
        factory = APIRequestFactory()
        request = factory.post("/api/planning/dagplanning/", {"date": "2023-03-31", "weekPlanning": self.wp})
        response = DagPlanningCreateAndListAPIView.as_view()(request).data
        self.assertEqual(response["date"], "2023-03-31")
        self.assertEqual(response["weekPlanning"], self.wp)
        self.assertIsNotNone(response["pk"])