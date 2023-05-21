import datetime

from rest_framework.test import APITestCase, APIRequestFactory, \
    force_authenticate, APIClient
from .views import *
from .models import *
from users.models import User
from ronde.models import Ronde, LocatieEnum
from io import BytesIO
from PIL import Image
from model_bakery import baker
from backend.views import MediaView


class CreateTest(APITestCase):
    def setUp(self) -> None:
        self.dp = baker.make(DagPlanning)
        self.ronde = baker.make(Ronde)
        self.ronde.save()
        self.ipb = InfoPerBuilding.objects.create(remark="test",
                                                  dagPlanning=self.dp)
        self.user = User.objects.create(role="SU")
        self.location = LocatieEnum.objects.create(name="Gent")
        self.student = User.objects.create(role="ST", username="student",
                                           email="s@s.s")
        self.studentTemplate = StudentTemplate.objects.create(name="test",
                                                              even=True,
                                                              location=self.location,
                                                              status=Status.EENMALIG,
                                                              year=2023,
                                                              week=1,
                                                              start_hour="19:13",
                                                              end_hour="19:14")

        templ = StudentTemplate.objects.create(name="test",
                                               even=datetime.datetime.now(

                                               ).isocalendar().week % 2 == 0,
                                               location=self.location,
                                               status=Status.EENMALIG,
                                               year=datetime.datetime.now().isocalendar().year,
                                               week=datetime.datetime.now(

                                               ).isocalendar().week,
                                               start_hour="19:13",
                                               end_hour="19:14"
                                               )

        self.weekPlanning = WeekPlanning.objects.create(week=1, year=2023)

        pl = WeekPlanning.objects.create(week=datetime.datetime.now(

        ).isocalendar().week,
                                         year=datetime.datetime.now(

                                         ).isocalendar().year)
        pl.student_templates.set([templ])

        self.pickupday = PickUpDay.objects.create(day="SU",
                                                  start_hour="19:13",
                                                  end_hour="19:14")
        self.dagPlanning = DagPlanning.objects.create(ronde=self.ronde,
                                                      time=self.pickupday)
        self.dagPlanning.students.set([self.student, self.user])
        self.studentTemplate.dag_planningen.set([self.dagPlanning])
        self.weekPlanning.student_templates.set([self.studentTemplate])
        self.studentTemplate.rondes.set([self.ronde])

    def testCreateStudentTemplate(self):
        # Create a student template
        factory = APIRequestFactory()
        date = datetime.datetime.now().isocalendar()
        request = factory.post("/api/studenttemplates/", {
            "location": self.location.id,
            "name": "Gent template even",
            "start_hour": "12:00",
            "end_hour": "13:00",
            "even": date.week % 2 == 0
        })
        force_authenticate(request, user=self.user)
        response = StudentTemplateView.as_view()(request).data
        self.assertIn("new_id", response)
        template_id = response["new_id"]

        # Get the newly created template
        request = factory.get(f'/api/studenttemplates/{template_id}/')
        force_authenticate(request, user=self.user)
        response = StudentTemplateView.as_view()(request, template_id).data
        self.assertIn("id", response[0])

        # Add a round to the template
        request = factory.post(f'/api/studenttemplates/{template_id}/rondes/',
                               {
                                   "ronde": self.ronde.id
                               })
        force_authenticate(request, user=self.user)

        response = RondesView.as_view()(request, template_id=template_id).data

        self.assertEqual(response["message"], "Success")

        request = factory.get(f'/api/studenttemplates/{template_id}/rondes/')
        force_authenticate(request, user=self.user)

        response = RondesView.as_view()(request, template_id=template_id).data

        self.assertIn("buildings", response[0])

        # Get the dayplans for this template
        days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
        request = factory.get(
            f'/api/studenttemplates/{template_id}/rondes/{self.ronde.id}/dagplanningen/')
        force_authenticate(request, user=self.user)
        response = DagPlanningenView.as_view()(request,
                                               template_id=template_id,
                                               ronde_id=self.ronde.id).data
        today = [x for x in response if
                 x["time"]["day"] == days[date.weekday - 1]]
        self.assertNotEquals(today, [])
        today = today[0]

        # Add a student to a dayplan of the template
        request = factory.patch(
            f'/api/studenttemplates/{template_id}/dagplanningen/{today["id"]}/',
            {
                "students": [self.student.id]
            })
        force_authenticate(request, user=self.user)
        response = DagPlanningView.as_view()(request, template_id=template_id,
                                             dag_id=today["id"],
                                             permanent=True).data
        self.assertEqual(response["message"], "Success")

        request = factory.get(f'/api/weekplanning/{date.year}/{date.week}/')
        force_authenticate(request, user=self.user)
        response = WeekplanningView.as_view()(request, year=date.year,
                                              week=date.week)
        self.assertEqual(response.status_code, 200)

        # Find the dayplan for a certain time
        request = factory.get(
            f'/api/dagplanning/{date.year}/{date.week}/{date.weekday}/')
        force_authenticate(request, user=self.student)
        response = StudentDayPlan.as_view()(request, year=date.year,
                                            week=date.week,
                                            day=date.weekday).data
        self.assertEqual(len(response), 1)
        self.assertEqual(
            StudentDayPlan.as_view()(request, year=date.year, week=date.week, \
                                     day=8).status_code,
            400)

        request = factory.get(
            f'studenttemplates/rondes/{date.year}/{date.week}/{date.weekday}/6/')
        force_authenticate(request, user=self.user)
        StudentTemplateRondeView.as_view()(request, year=date.year,
                                           week=date.week,
                                           day=date.weekday, location=6)

        request = factory.patch(
            f'/api/studenttemplates/{template_id}/dagplanningen/{today["id"]}/eenmalig/',
            {
                "students": []
            })
        force_authenticate(request, user=self.user)
        DagPlanningView.as_view()(request, template_id=template_id,
                                  dag_id=today["id"],
                                  permanent=False)

        request = factory.get('/api/studenttemplates/')
        force_authenticate(request, user=self.user)
        templates = StudentTemplateView.as_view()(request).data
        for template in templates:
            request = factory.patch(f'/api/studenttemplates/{template["id"]}/',
                                    {
                                        "start_hour": "11:00",
                                        "end_hour": "14:00"
                                    })
            force_authenticate(request, user=self.user)
            StudentTemplateView.as_view()(request, template["id"])

        request = factory.get('/api/studenttemplates/')
        force_authenticate(request, user=self.user)
        templates = StudentTemplateView.as_view()(request).data
        for template in templates:
            request = factory.delete(
                f'/api/studenttemplates/{template["id"]}/')
            force_authenticate(request, user=self.user)
            StudentTemplateView.as_view()(request, template["id"])

    def testInfoPerBuilding(self):
        # An error should be returned if an invalid dayplanning query is given
        factory = APIRequestFactory()
        request = factory.get('/api/infoperbuilding?dagPlanning=9')
        force_authenticate(request, user=self.user)
        response = InfoPerBuildingCLAPIView.as_view()(request).data
        self.assertIn("errors", response)

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
        picture_id = response["id"]

        request = factory.get(response["image"])
        path = (response["image"].split("/"))[-1]
        force_authenticate(request, self.user)
        response = MediaView.as_view()(request, path=path)
        self.assertEqual(response.status_code, 200)

        # Fetch the uploaded picture
        request = factory.get('/api/buildingpicture/')
        force_authenticate(request, user=self.user)
        response = BuildingPictureCreateAndListAPIView.as_view()(request).data
        self.assertIn("id", response[0])
        request = factory.get(
            '/api/buildingpicture?infoPerBuilding=9&year=2002&week=11')
        force_authenticate(request, user=self.user)
        response = BuildingPictureCreateAndListAPIView.as_view()(request).data
        self.assertIn("errors", response)

        # Patch the uploaded picture
        request = factory.patch(f'/api/buildingpicture/{picture_id}/', {
            "remark": "testRemark 2",
        })
        force_authenticate(request, user=self.user)
        response = BuildingPictureRUDAPIView.as_view()(request,
                                                       pk=picture_id).data
        self.assertIn("id", response)
        self.assertEqual(response["remark"], "testRemark 2")
        # Put the uploaded picture
        file = BytesIO()
        image = Image.new('RGBA', size=(10, 10), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        request = factory.put(f'/api/buildingpicture/{picture_id}/', {
            "pictureType": "ST",
            "image": file,
            "time": "2002-03-27 22:33",
            "remark": "testRemark 2",
            "infoPerBuilding": self.ipb.pk
        })
        force_authenticate(request, user=self.user)
        response = BuildingPictureRUDAPIView.as_view()(request,
                                                       pk=picture_id).data
        self.assertIn("id", response)

    def testGetWeekPlanning(self):
        factory = APIRequestFactory()
        request = factory.get("/api/weekplanning/2023/1")
        force_authenticate(request, user=self.user)
        response = WeekplanningView.as_view()(request, year=2023, week=1).data
        # geen studenttemplates die bij de ronde horen
        self.assertEqual(len(response), 1)

    def testGetDagPlanning(self):
        factory = APIRequestFactory()
        request = factory.get("/api/dagplanning/2023/1/1/")
        force_authenticate(request, self.student)
        response = StudentDayPlan.as_view()(request, year=2023, week=1,
                                            day=0).data
        self.assertEqual(len(response), 1)

    def testGetDagPlanning(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/dagplanning/{self.dagPlanning.pk}/")
        force_authenticate(request, self.user)
        response = DagPlanningRetrieveUpdateAPIView.as_view()(request,
                                                              pk=self.dagPlanning.pk).data

        self.assertIn("id", response)

    def testGetPlanningStatus(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/dagplanning/2023/1/"
                              f"{self.dagPlanning.pk}/status/")
        force_authenticate(request, self.user)
        response = planning_status(request, year=2023,
                                   week=1,
                                   pk=self.dagPlanning.pk).data
        self.assertEqual(type(response), dict)

    def testGetPlanningPictures(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/dagplanning/2023/1/"
                              f"{self.dagPlanning.pk}/pictures/")
        force_authenticate(request, self.user)
        response = planning_pictures(request, year=2023,
                                     week=1,
                                     pk=self.dagPlanning.pk).data
        self.assertEqual(type(response), dict)

    def testGetTemplateForPlanning(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/find/planning/"
                              f"{self.dagPlanning.pk}/")
        force_authenticate(request, self.user)
        response = template_for_planning(request, pk=self.dagPlanning.pk).data
        self.assertIn("template_id", response)

    def testStudentTemplateRondeTime(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/rondes/2023/1/1/"
                              f"{self.location.pk}")
        force_authenticate(request, self.user)
        response = StudentTemplateRondeView.as_view()(request, year=2023,
                                                      week=1, day=1,
                                                      location=self.location.pk)
        self.assertEqual(response.status_code, 200)

    def testStudentTemplates(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/")
        force_authenticate(request, self.user)
        response = StudentTemplateView.as_view()(request).data
        # template is niet actief
        self.assertEqual(len(response), 0)

    def testStudentTemplate(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/")
        force_authenticate(request, self.user)
        response = StudentTemplateDetailView.as_view()(request,
                                                       template_id=self.studentTemplate.pk)
        self.assertEqual(response.data["id"], self.studentTemplate.id)

    def testStudentTemplatesRondes(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/rondes")
        force_authenticate(request, self.user)
        response = RondesView.as_view()(request,
                                        template_id=self.studentTemplate.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.ronde.id)

    def testStudentTemplateRonde(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/rondes/"
                              f"{self.ronde.pk}/")
        force_authenticate(request, self.user)
        response = RondeView.as_view()(request,
                                       template_id=self.studentTemplate.pk,
                                       ronde_id=self.ronde.pk)
        # get not supported
        self.assertEqual(response.status_code, 405)

    def testStudentTemplateDagPlanningen(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/"
                              f"rondes/{self.ronde.pk}/"
                              f"dagplanningen/")
        force_authenticate(request, self.user)
        response = DagPlanningenView.as_view()(request, template_id=
        self.studentTemplate.pk, ronde_id=self.ronde.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.dagPlanning.pk)

    def testStudentTemplateDagPlanningPermanent(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/dagplanningen/"
                              f"{self.dagPlanning.pk}/")
        force_authenticate(request, self.user)
        response = DagPlanningView.as_view()(request,
                                             template_id=self.studentTemplate.pk,
                                             dag_id=self.dagPlanning.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.dagPlanning.pk)

    def testStudentTemplateDagPlanningNonPermanent(self):
        factory = APIRequestFactory()
        request = factory.get(f"/api/studenttemplates/"
                              f"{self.studentTemplate.pk}/dagplanningen/"
                              f"{self.dagPlanning.pk}/eenmalig/")
        force_authenticate(request, self.user)
        response = DagPlanningView.as_view()(request,
                                             template_id=self.studentTemplate.pk,
                                             dag_id=self.dagPlanning.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.dagPlanning.pk)
