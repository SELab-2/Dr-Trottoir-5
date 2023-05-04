from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import *
from .models import *
from users.models import User
from ronde.models import Ronde, LocatieEnum
from io import BytesIO
from PIL import Image
from model_bakery import baker


class CreateTest(APITestCase):

    def setUp(self) -> None:
        self.dp = baker.make(DagPlanning)
        self.ronde = baker.make(Ronde)
        self.ronde.save()
        self.ipb = InfoPerBuilding.objects.create(remark="test", dagPlanning=self.dp)
        self.user = User.objects.create(role="SU")
        self.location = LocatieEnum.objects.create(name="Gent")
        self.student = User.objects.create(role="ST", username="student", email="s@s.s")

    def testCreateStudentTemplate(self):
        # Create a student template
        factory = APIRequestFactory()
        request = factory.post("/api/studenttemplates/", {
            "location": self.location.id,
            "name": "Gent template even",
            "start_hour": "12:00",
            "end_hour": "13:00",
            "even": True
        })
        force_authenticate(request, user=self.user)
        response = student_templates_view(request).data
        self.assertIn("new_id", response)
        template_id = response["new_id"]

        # Get the newly created template
        request = factory.get(f'/api/studenttemplates/{template_id}/')
        force_authenticate(request, user=self.user)
        response = student_template_view(request, template_id).data
        self.assertIn("id", response)

        # Add a round to the template
        request = factory.post(f'/api/studenttemplates/{template_id}/rondes/', {
            "ronde": self.ronde.id
        })
        force_authenticate(request, user=self.user)
        response = rondes_view(request, template_id).data
        self.assertEqual(response["message"], "Success")

        request = factory.get(f'/api/studenttemplates/{template_id}/rondes/')
        force_authenticate(request, user=self.user)
        response = rondes_view(request, template_id).data
        self.assertIn("buildings", response[0])

        # Get the dayplans for this template
        date = datetime.datetime.now().isocalendar()
        days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        request = factory.get(f'/api/studenttemplates/{template_id}/rondes/{self.ronde.id}/dagplanningen/')
        force_authenticate(request, user=self.user)
        response = dagplanningen_view(request, template_id, self.ronde.id).data
        today = [x for x in response if x["time"]["day"] == days[date.weekday - 1]]
        self.assertNotEquals(today, [])
        today = today[0]

        # Add a student to a dayplan of the template
        request = factory.patch(f'/api/studenttemplates/{template_id}/dagplanningen/{today["id"]}/', {
            "students": [self.student.id]
        })
        force_authenticate(request, user=self.user)
        response = dagplanning_view(request, template_id, today["id"], True).data
        self.assertEqual(response["message"], "Success")

        # Find the dayplan for a certain time
        request = factory.get(f'/api/dagplanning/{date.year}/{date.week}/{date.weekday}/')
        force_authenticate(request, user=self.student)
        response = student_dayplan(request, date.year, date.week, date.weekday).data
        self.assertIn("id", response)
        self.assertEqual(student_dayplan(request, date.year, date.week, 8).status_code, 400)


    def testAddBuildingPicture(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        factory = APIRequestFactory()
        request = factory.post("/api/buildingpicture/", {
            "pictureType": "ST",
            "image": file,
            "time": "2002-03-27 22:33",
            "remark": "testRemark",
            "infoPerBuilding": self.ipb.pk
        })
        force_authenticate(request, user=self.user)
        response = BuildingPictureCreateAndListAPIView.as_view()(request).data
        self.assertEqual(response["pictureType"], "ST")
        self.assertIsNotNone(response.get("image"))
        self.assertEqual(response["time"], "2002-03-27T22:33:00+01:00")
        self.assertEqual(response["remark"], "testRemark"),
        self.assertEqual(response["infoPerBuilding"], self.ipb.pk)
        self.assertIsNotNone(response["id"])
