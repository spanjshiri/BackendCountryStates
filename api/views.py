from django.shortcuts import render
from .models import Country
from rest_framework.generics import ListAPIView
from .serializers import CountrySerializer

class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

