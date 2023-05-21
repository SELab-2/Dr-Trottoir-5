from rest_framework.test import APITestCase, APIRequestFactory, \
    force_authenticate

from mailtemplates.views import *
from django.contrib.auth import get_user_model


class MailTemplateTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(role="SU")

    def testCreate(self):
        factory = APIRequestFactory()
        request = factory.get("/api/mailtemplates/")
        force_authenticate(request, self.user)
        response = MailTemplateCreateAndListView.as_view()(request).data
        self.assertEqual(len(response), 0)

        request = factory.post("/api/mailtemplates/",
                               {
                                   "name": "test",
                                   "content": "test content"
                               })
        force_authenticate(request, self.user)
        response = MailTemplateCreateAndListView.as_view()(request).data
        self.assertIn("id", response)

        request = factory.get("/api/mailtemplates/")
        force_authenticate(request, self.user)
        response = MailTemplateCreateAndListView.as_view()(request).data
        self.assertEqual(len(response), 1)

    def testGet(self):
        factory = APIRequestFactory()
        # create template
        request = factory.post("/api/mailtemplates/",
                               {
                                   "name": "test",
                                   "content": "test content"
                               })
        force_authenticate(request, self.user)
        response = MailTemplateCreateAndListView.as_view()(request).data
        id = response["id"]

        request = factory.get(f"/api/mailtemplates/{id}/")
        force_authenticate(request, self.user)
        response = MailTemplateRetrieveUpdateDestroyAPIView.as_view()(
            request, pk=id)
        self.assertEqual(response.status_code, 200)

    def testPatch(self):
        factory = APIRequestFactory()
        # create template
        request = factory.post("/api/mailtemplates/",
                               {
                                   "name": "test",
                                   "content": "test content"
                               })
        force_authenticate(request, self.user)
        response = MailTemplateCreateAndListView.as_view()(request).data
        id = response["id"]

        request = factory.patch(f"/api/mailtemplates/{id}/",
                                {
                                    'name': 'updated name'
                                })
        force_authenticate(request, self.user)
        response = MailTemplateRetrieveUpdateDestroyAPIView.as_view()(
            request, pk=id)
        self.assertLess(response.status_code, 400)
        self.assertEqual(response.data["name"], "updated name")
