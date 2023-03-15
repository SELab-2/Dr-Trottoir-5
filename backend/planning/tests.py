from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory
from .views import *
from .models import *

from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.


class CreateTest(APITestCase):

    def setUp(self) -> None:
        self.wp = WeekPlanning.objects.create(week=0, year=2023)
        self.dp = DagPlanning.objects.create(date="2023-08-31", weekPlanning=self.wp)
        self.ipb = InfoPerBuilding.objects.create(remark="test", dagPlanning=self.dp)

    def testAddWeekPlanning(self):
        factory = APIRequestFactory()
        request = factory.post("/api/planning/weekplanning/", {"week": 12, "year": 2023})
        response = WeekPlanningCLAPIView.as_view()(request).data
        self.assertEqual(response["week"], 12)
        self.assertEqual(response["year"], 2023)
        self.assertIsNotNone(response.get("id"))

    def testAddDagPlanning(self):
        factory = APIRequestFactory()
        request = factory.post("/api/planning/dagplanning/", {"date": "2023-03-31", "weekPlanning": self.wp.pk})
        response = DagPlanningCreateAndListAPIView.as_view()(request).data
        self.assertEqual(response["date"], "2023-03-31")
        self.assertEqual(response["weekPlanning"], self.wp.pk)
        print(response)
        self.assertIsNotNone(response.get("id"))

    def testAddInfoPerBuilding(self):
        factory = APIRequestFactory()
        request = factory.post("/api/planning/infoperbuilding/", {
            "remark": "This is a test remark",
            "dagPlanning": self.dp.pk
        })
        response = InfoPerBuildingCLAPIView.as_view()(request).data
        self.assertEqual(response["remark"], "This is a test remark")
        self.assertEqual(response["dagPlanning"], self.dp.pk)
        self.assertIsNotNone(response.get("id"))

    def testAddBuildingPicture(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        factory = APIRequestFactory()
        request = factory.post("/api/planning/buildingpicture/", {
            "pictureType": "ST",
            "image": file,
            "time": "2002-03-27 22:33",
            "remark": "testRemark",
            "infoPerBuilding": self.ipb.pk
        })
        response = BuildingPictureCreateAndListAPIView.as_view()(request).data
        self.assertEqual(response["pictureType"], "ST")
        self.assertIsNotNone(response.get("image"))
        self.assertEqual(response["time"], "2002-03-27T22:33:00+01:00")
        self.assertEqual(response["remark"], "testRemark"),
        self.assertEqual(response["infoPerBuilding"], self.ipb.pk)
        self.assertIsNotNone(response["id"])
