from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import LocatieEnum


class CreateTest(APITestCase):

    def test_with_no_name_attr(self):
        """
            Check if we can't create a location without name attribute
        """
        url = '/api/ronde/locatie'
        data = {}
        response = self.client.post(url, data, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_402_PAYMENT_REQUIRED)

    def test_with_empty_name(self):
        """
            Check if we can't create a location without name attribute
        """
        url = '/api/ronde/locatie'
        data = {'name': ''}
        response = self.client.post(url, data, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
