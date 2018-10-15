from rest_framework.serializers import ModelSerializer, IntegerField
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

    country_code = IntegerField(source='country.code')

    class Meta:
        model = State
        fields = '__all__'

    def create(self, validated_data):
        print ('\n\n\n\n\nValidated_Data:' + str(validated_data) + '\n\n\n\n\n')
        country = validated_data.pop('country_code')
        country = get_object_or_404(Country, code=country)
        state = State.objects.create(**validated_data, country=country)
        return state