from django.urls import path
from .views import service,service_detail
app_name = 'service'

urlpatterns = [
    path('',service,name='service'),
    path('/category/<str:category>',service,name='service_category'),
    path('/detail/<int:id>',service_detail,name='service_detail'),

]