from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from api.tasks import test_task

# Create your views here.

class Test(views.APIView):
    def get(self, request):
        test_task.delay(100,5)
        return Response("Celery Task Running")