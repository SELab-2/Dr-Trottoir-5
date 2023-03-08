from .models import TrashContainer
from django.views.decorators.csrf import csrf_exempt
from .serializers import TrashContainerSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def trashcontainers(request):
    """
        Handle requests for trashcontainers
    """
    if request.method == 'GET':
        containers = TrashContainer.objects.all()
        serializer = TrashContainerSerializer(containers, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrashContainerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def trashcontainers_pk(request, pk):
    try:
        container = TrashContainer.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrashContainerSerializer(container)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrashContainerSerializer(container, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        container.delete()
        return HttpResponse(status=204)
