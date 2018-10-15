from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import Country, State
from django.shortcuts import get_object_or_404

class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(ModelSerializer):

    countryId = IntegerField(source='country.id', required=False)

    class Meta:
        model = State
        exclude = ['country']
        
class StateCreateSerializer(ModelSerializer):

    country_code = CharField(source='country.code')

    class Meta:
        model = State
        fields = ['code','name','country_code']

    def create(self, validated_data):
        print ('\n\n\n\n\nValidated_Data:' + str(validated_data) + '\n\n\n\n\n')
        country_object = validated_data.pop('country')
        country = country_object.pop('code')
        country = get_object_or_404(Country, code=country)
        state = State.objects.create(**validated_data, country=country)
        return state