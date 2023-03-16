from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import LocatieEnumListCreateView, RondeListCreateView
from .models import LocatieEnum, Ronde
from users.models import User


class TestApi(TestCase):

    def setUp(self):
        self.user = User.objects.create(role="SU")
        LocatieEnum.objects.create(name="Gent")
        Ronde.objects.create(name="TestRonde", location=LocatieEnum.objects.get(name="Gent"))

    def test_add_locatie(self):
        """
            Test for adding a location
        """
        factory = APIRequestFactory()
        request = factory.post('/api/ronde/locatie/', {'name': 'Oostende'})
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data
        self.assertEqual(response["succes"]["id"], 2)
        self.assertEqual(response["succes"]["name"], "Oostende")

    def test_get_locaties(self):
        """
            Test to get location back
        """
        factory = APIRequestFactory()
        request = factory.get('/api/ronde/locatie/')
        force_authenticate(request, user=self.user)
        response = LocatieEnumListCreateView.as_view()(request).data
        self.assertNotEquals(len(response), 0)

    def test_get_rondes(self):
        """
            Test for getting Ronde
        """
        factory = APIRequestFactory()
        request = factory.get('/api/ronde/')
        force_authenticate(request, user=self.user)
        response = RondeListCreateView.as_view()(request).data
        self.assertNotEquals(len(response), 0)
