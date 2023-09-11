from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.response import Response
import requests
from rest_framework.decorators import action

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
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = Activity.objects.all()

        # Retrieve filter parameters from the query string
        # id = request.query_params.get('id') 
        activity_type = request.query_params.get('type')
        participants = request.query_params.get('participants')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        min_accessibility = request.query_params.get('min_accessibility')
        max_accessibility = request.query_params.get('max_accessibility')

        # Apply filters if parameters are provided
        
        # if id:
        #     queryset = queryset.filter(activity.data['id']=activity_type)
        if activity_type:
            queryset = queryset.filter(type=activity_type)
        if participants:
            queryset = queryset.filter(participants=participants)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        if min_accessibility is not None:
            queryset = queryset.filter(accessibility__gte=min_accessibility)  # Use 'accessibility' field here
        if max_accessibility is not None:
            queryset = queryset.filter(accessibility__lte=max_accessibility)  # Use 'accessibility' field here

        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def latest_activities(self, request):
        """
        Retrieve the latest activities saved in the database.
        """
        num_activities = request.query_params.get('num_activities', 5)  # Default to 5 if not provided
        try:
            num_activities = int(num_activities)
        except ValueError:
            return Response({"error": "Invalid num_activities parameter. It must be an integer."}, status=400)

        latest_activities = Activity.objects.order_by('-id')[:num_activities]
        serializer = ActivitySerializer(latest_activities, many=True)
        return Response(serializer.data)
