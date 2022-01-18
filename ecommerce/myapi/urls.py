from django.urls import include, path

from django.contrib import admin

from myapi.views import *



urlpatterns = [
   path('species/', SpeciesGeneric.as_view()),
   path('people/', PersonGeneric.as_view()),
   path('people/<int:pk>/', PersonGenericDetail.as_view()),
   path('species/<int:pk>', SpeciesGenericDetail.as_view()),

]