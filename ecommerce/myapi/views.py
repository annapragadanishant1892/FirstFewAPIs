from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from django.http import Http404
from rest_framework import status


from myapi.filters import *
from django_filters import rest_framework as filters

from myapi.serializers import *
from myapi.models import Person, Species
from rest_framework.response import Response

class PersonGeneric(generics.GenericAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class= BirthFilter


    def filter_data(self, request):
        qs = Person.objects.all()
        filtered_data = BirthFilter(request.GET, queryset=qs)
        filtered_qs = filtered_data.qs
        return filtered_qs

    def get(self, request):
        instance= self.queryset.all()
        serializer=self.serializer_class(instance, many= True)
        data=serializer.data
        return Response(data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonGenericDetail(generics.GenericAPIView):
    serializer_class = PersonSerializer

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class SpeciesGeneric(generics.GenericAPIView):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def get(self, request):
        instance = self.queryset.all()
        serializer = self.serializer_class(instance, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = SpeciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeciesGenericDetail(generics.GenericAPIView):
    serializer_class = SpeciesSerializer

    def get_object(self, pk):
        try:
            return Species.objects.get(pk=pk)
        except Species.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







