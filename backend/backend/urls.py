"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include('users.urls')),
    path('api/planning/', include('planning.urls')),
    path('api/containers/', include('trashcontainers.urls')),
    path('api/pickupdays/', include('pickupdays.urls')),
    path('api/mailtemplates/', include('mailtemplates.urls')),
    path('api/ronde/', include('ronde.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
