from django.shortcuts import get_object_or_404
from .models import Country, State
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import CountrySerializer, StateSerializer, StateCreateSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class CountryList(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StatesOfCountryList(APIView):
    def get(self, request, format=None, **kwargs):
        code = self.kwargs['country_code']
        country = get_object_or_404(Country, code=code)
        states = country.states.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, **kwargs):
        country = kwargs['country_code']
        state_data = request.data
        state_data['country_code'] = country
        serializer = StateCreateSerializer(data=state_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

