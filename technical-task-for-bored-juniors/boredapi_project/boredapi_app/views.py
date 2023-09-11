from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
import requests

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def create(self, request, *args, **kwargs):
        response = requests.get('https://www.boredapi.com/api/activity')
        data = response.json()
        activity = Activity(
            activity=data['activity'],
            type=data['type'],
            participants=data['participants'],
            price=data['price'],
            key=data['key']
        )
        activity.save()
        serializer = ActivitySerializer(activity)
        return HttpResponse(serializer.data)
