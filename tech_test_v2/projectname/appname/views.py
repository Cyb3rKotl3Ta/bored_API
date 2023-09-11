from django.shortcuts import render
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['GET'])
    def retrieve_record(self, request, pk=None):
        try:
            record = self.queryset.get(pk=pk)
            serializer = self.serializer_class(record)
            return Response(serializer.data)
        except MyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(detail=True, methods=['DELETE'])
    def delete_record(self, request, pk=None):
        try:
            record = self.queryset.get(pk=pk)
            record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MyModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    