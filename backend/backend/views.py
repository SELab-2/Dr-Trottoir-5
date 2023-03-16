from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.views.static import serve
from django.conf import settings


class MediaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, path):
        return serve(request, path, document_root=settings.MEDIA_ROOT)
