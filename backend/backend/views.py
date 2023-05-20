from django.conf import settings
from django.views.static import serve
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class MediaView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, path):
        return serve(request, path, document_root=settings.MEDIA_ROOT)
