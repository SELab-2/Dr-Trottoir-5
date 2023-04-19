from django.test import TestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import LocatieEnumListCreateView, RondeListCreateView, \
    ManualListCreateView, LocatieEnumRetrieveDestroyView
from .models import LocatieEnum, Ronde
from users.models import User
from io import BytesIO


class TestApi(TestCase):

    def setUp(self):
        self.user = User.objects.create(role="SU")
        LocatieEnum.objects.create(name="Gent")
        Ronde.objects.create(name="TestRonde",
                             location=LocatieEnum.objects.get(name="Gent"))

    def testAddLocation(self):
        """
            Test for adding a location
        """
        factory = APIRequestFactory()
        request = factory.post('/api/ronde/locatie/', {})
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data

        # returns an error
        self.assertIn("errors", response)
        self.assertEqual(response["errors"][0]["field"], ErrorDetail(
            string="name", code="invalid"))

        request = factory.post('/api/ronde/locatie/', {"name": ""})
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data

        self.assertIn("errors", response)

        request = factory.post('/api/ronde/locatie/', {'name': 'Oostende'})
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data

        self.assertEqual(response["succes"]["name"], "Oostende")

    def testGetLocations(self):
        """
            Test to get location back
        """
        factory = APIRequestFactory()
        request = factory.get('/api/ronde/locatie/')
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data
        self.assertNotEquals(len(response), 0)

    def testGetLocation(self):
        factory = APIRequestFactory()
        request = factory.post('/api/ronde/locatie/', {'name': 'Oostende'})
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data

        request = factory.get(
            f'/api/ronde/locatie/{response["succes"]["id"]}/')
        force_authenticate(request, user=self.user)
        response = LocatieEnumRetrieveDestroyView\
            .as_view()(request, pk=response["succes"]["id"]).data
        self.assertEqual(response["name"], "Oostende")

    def testGetRondes(self):
        """
            Test for getting Ronde
        """
        factory = APIRequestFactory()
        request = factory.get('/api/ronde/')
        force_authenticate(request, user=self.user)
        response = RondeListCreateView.as_view()(request).data
        self.assertNotEquals(len(response), 0)

    def testUploadManual(self):
        """
            Test if we can upload a manual for a building
        """
        factory = APIRequestFactory()
        file = BytesIO()
        file.write(b'test')
        file.seek(0)

        # Test normal upload
        request = factory.post('/api/building/manual/',
                               {"manualStatus": "Klaar", "fileType": "PDF",
                                "file": file})
        force_authenticate(request, user=self.user)
        response = ManualListCreateView.as_view()(request).data
        self.assertEqual(response["succes"]["manualStatus"], "Klaar")

        # Test upload with missing argument
        request = factory.post('/api/building/manual/',
                               {"manualStatus": "Klaar", "file": file})
        force_authenticate(request, user=self.user)
        response = ManualListCreateView.as_view()(request).data
        self.assertIn("errors", response)

        # Test upload with empty argument
        request = factory.post('/api/building/manual/',
                               {"manualStatus": "Klaar", "fileType": "",
                                "file": file})
        force_authenticate(request, user=self.user)
        response = ManualListCreateView.as_view()(request).data
        self.assertIn("errors", response)

        # Test upload with wrong argument
        request = factory.post('/api/building/manual/',
                               {"manualStatus": "Done", "fileType": "PDF",
                                "file": file})
        force_authenticate(request, user=self.user)
        response = ManualListCreateView.as_view()(request).data
        self.assertIn("errors", response)
