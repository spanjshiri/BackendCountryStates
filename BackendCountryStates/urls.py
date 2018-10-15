from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.views.generic.base import RedirectView
from django.conf.urls import url, include
from api.views import CountryList, StateList, StatesOfCountryList

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/countries', permanent=False), name='index'),
    path('api/countries/', CountryList.as_view(), name='country_list'),
    path('api/states/', StateList.as_view(), name='state_list'),
    path('api/countries/<str:country_code>/states/', StatesOfCountryList.as_view(), name='state_of_country_list')
]
