from django.urls import path
from .views import properties,properties_detail
app_name = 'properties'
urlpatterns = [
    path('properties',properties,name='properties'),
    path('properties_detail',properties_detail,name ='properties_detail')
]