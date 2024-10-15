from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

from api.tasks import sum, mul

from celery.result import AsyncResult


# Create your views here.

class Test(views.APIView):
    def get(self, request):
        sum.delay(100,5)
        mul.delay(100,5)
        return Response("Celery Task Running")
        # task1 = sum.delay(100,5)
        # task2 = mul.delay(100,5)
        # return Response({"task1_id": task1.id, "task2_id":task2.id}, status=202)
    

